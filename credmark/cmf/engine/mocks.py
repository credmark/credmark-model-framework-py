import logging
import os
from typing import List, Union
from credmark.cmf.model.errors import ModelBaseError, ModelDataError
from credmark.dto import DTOType


class ModelMockException(Exception):
    pass


class ModelMock:
    """
    Defines mock output for a model and options for how the mock is used.

    Parameters:
        output: A dictionary where the keys are model slugs and the
                values are one or more outputs. *(See details below.)*

        input: None or a dict containing a (full or partial) model input.
               *(See details below.)*

        repeat: a count of times to repeat the output. Defaults to 0 which
               is unlimited repeats.


    The values in the ``output`` dictionary can be:

        - a string representing the slug of an actual model to run

        - a dict representing the output from a call to run_model(slug).

        - a DTO instance representing the output from a call to run_model(slug).

        - a ModelBaseError subclass instance representing an error that will be raised

        - a ModelMock instance to use as the output.

        - a list of dicts, DTOs, errors, or strings (as described above),
          representing the outputs to iterate over for each to call run_model(slug).

    An ``input`` dict can contain a full or partial model input
    where if the input values match the input passed to run_model(slug),
    it is considered a match and the output is used. *(Currently only
    a top-level shallow comparison of input values is used.)*

    **NOTE**: Mocks in the top-level list (outside a ModelMock instance) for
    a slug in the config that have ``input`` set will be used as a *lookup*
    before using other mocks in the list. Any Mocks with no input match criteria
    will be used after all mocks containing input are tried and there was no
    match. For mocks that are not in the top-level list for a slug, the input is
    simply used as a filter before a mock is used, in the normal order.

    """

    def __init__(self,
                 output: Union[dict, DTOType, ModelBaseError, str,
                               List[Union[dict, DTOType, ModelBaseError, str, 'ModelMock']]],
                 input: Union[dict, None] = None,
                 repeat=0):

        self.output = output
        self.input = input
        self.repeat = repeat

    def __repr__(self):
        # output valid python to create the mock
        if isinstance(self.output, ModelBaseError):
            cls = self.output.__class__.__name__
            data = self.output.data.dict().copy()
            del data['type']
            return (f'ModelMock({cls}(**{data}),' +
                    f'input={self.input}, repeat={self.repeat})')
        elif isinstance(self.output, str):
            return f'ModelMock("{self.output}", input={self.input}, repeat={self.repeat})'
        else:
            return f'ModelMock({self.output}, input={self.input}, repeat={self.repeat})'

    @classmethod
    def check_input_match(cls, model_input: dict, match_input: dict):
        for k, v in match_input.items():
            if model_input.get(k) != v:
                return False
        return True


class ModelMockConfig:
    """
    Configuration of mock models.

    Parameters:
        ``models`` (dict): a dict where each key is a model slug and the
            value is a ModelMock instance or list of ModelMock instances.

        ``run_unmocked`` (boolean): If true, an unmocked model will be run normally.
            Otherwise an exception will be raised.

    Example::

        config = ModelMockConfig(
            run_unmocked=False,  # unmocked models cannot be run

            models={
                "example.echo": ModelMock("example.echo"),
                "contrib.a": ModelMock({"a": 42}),
                "contrib.b": ModelMock([{"b": 1}, {"b": 2}, "contrib.b"]),
                "contrib.b-rep": ModelMock([{"b": 1}, {"b": 2},
                                            "contrib.b-rep"], repeat=2),
                "contrib.c": ModelMock({"c": 42}, input={"address": "0x00000000"}, repeat=2),
                "contrib.d": ModelMock([{"d": 1}, {"d": 2}],
                                    input={"address": "0x00000000"}),
                "contrib.e": [ModelMock({"e": 42}, input={"address": "0x00000000"}),
                            ModelMock({"e": 1})],
                "contrib.f": [ModelMock({"f": 42}, input={"address": "0x00000000"}),
                            ModelMock("contrib.f")],
                "contrib.g": ModelMock([ModelMock({"g": 1}, repeat=1),
                                        ModelMock({"g": 2}, repeat=2),
                                        ModelMock({"g": 3}, repeat=3)],
                                    repeat=2),
                "contrib.h": ModelMock(ModelDataError('Mock data error')),
            }
        )

    When using model mocks, all run model calls will try to use a mock.
    If there is no entry or input-matching entry for a run_model slug and
    ``run_unmocked`` is False, an exception will be raised.
    """

    def __init__(self,
                 models: dict[str, Union[ModelMock, List[ModelMock]]],
                 run_unmocked=False):
        self.models = models
        self.run_unmocked = run_unmocked


class MockEntryCursorFrame:
    def __init__(self, index=0, repeat=0):
        self.index = index
        self.repeat = repeat

    def __repr__(self):
        return f'(index={self.index} repeat={self.repeat})'


class MockGenerator:
    """
    Generate mocks for model runs and write python to a file.

    The model_run() method should be called for each run and a
    mock will be created for it.

    Example usage:

        gen = MockGenerator()
        EngineModelContext.add_model_run_listener(gen.model_run)

        EngineModelContext.create_context_and_run_model(model_slug=model_slug...)

        gen.write('mocks.py', model_slug)
    """

    def __init__(self):
        self.model_map = {}
        self.error_classes = set()

    def write(self, file_path: str, omit_slug: str):
        with open(file_path, 'w') as file:
            self._write_header(file)
            slugs = [slug for slug in self.model_map if slug != omit_slug]
            slugs.sort()
            count = len(slugs)

            for i, slug in enumerate(slugs):
                mocks = self.model_map[slug]
                file.write(f'        \'{slug}\': {mocks}{"," if i < count - 1 else ""}\n')

            self._write_footer(file)

    def _write_header(self, file):
        if len(self.error_classes) > 0:
            file.write(f'from credmark.cmf.model.errors import {", ".join(self.error_classes)}\n')
        file.write('from credmark.cmf.engine.mocks import ModelMock, ModelMockConfig\n\n\n')
        file.write('mocks = ModelMockConfig(\n')
        file.write('    run_unmocked=False,\n')
        file.write('    models={\n')

    def _write_footer(self, file):
        file.write('    }\n')
        file.write(')\n')

    def model_run(self,
                  slug: str,
                  _version: Union[str, None],
                  _chain_id: int,
                  _block_number: int,
                  _input: Union[dict, DTOType, None],
                  output: Union[dict, DTOType, None],
                  error: ModelBaseError):
        if slug not in self.model_map:
            self.model_map[slug] = []

        if error is not None:
            self.error_classes.add(error.__class__.__name__)

        self.model_map[slug].append(ModelMock(output if output is not None else error, repeat=1))


class MockEntryCursor:
    def __init__(self):
        self.cursor_stack: List[MockEntryCursorFrame] = []

    def __str__(self):
        return str(self.cursor_stack)

    def next_output(self,  # pylint: disable=too-many-branches
                    mocks: Union[ModelMock, List[ModelMock]],
                    model_input: dict,
                    depth=0,
                    loop=0) -> Union[dict, DTOType, str, ModelBaseError, None]:
        # If a list (and not a mock), we don't repeat
        repeat = mocks.repeat if isinstance(mocks, ModelMock) else 1

        if depth == len(self.cursor_stack):
            self.cursor_stack.append(MockEntryCursorFrame(0, 0))

        cursor = self.cursor_stack[depth]

        if isinstance(mocks, list):
            # list of mocks
            outputs = mocks
        else:
            if mocks.input and not ModelMock.check_input_match(model_input, mocks.input):
                return None
            outputs = mocks.output

        if isinstance(outputs, list):
            count = len(outputs)
            if count > 0 and (repeat == 0 or cursor.repeat < repeat):
                while cursor.index < count:
                    output = outputs[cursor.index]
                    if isinstance(output, ModelMock):
                        output = self.next_output(output, model_input, depth + 1)
                        if output is None:
                            # Mock output is exhausted
                            self.cursor_stack.pop(depth + 1)
                            cursor.index += 1
                    else:
                        # Output element is used to go to next
                        cursor.index += 1

                    if output is not None:
                        return output
                # Try repeating the whole list (same depth)
                cursor.index = 0
                cursor.repeat += 1
                if loop < 1:
                    return self.next_output(mocks, model_input, depth, loop + 1)
            return None
        else:
            if repeat == 0 or cursor.repeat < repeat:
                cursor.repeat += 1
                return outputs
        return None


class ModelMockRunner:
    """
    Mock model outputs based on slug and optionally, input parameters.

    Uses a MockModelConfig to configure the mocks.

    """

    logger = logging.getLogger(__name__)

    def __init__(self, mock_config_module_name: Union[str, None] = None):
        """
        Params:
        mock_config_module_name: A module and symbol name in dot syntax
        (ex. "models.contrib.mymodels.mymocks.mockconfig"), where the
        last element is a symbol whose value is a ModelMockConfig instance.
        """
        self._slug_entry_list_map: dict[str, List[ModelMock]] = {}
        self._slug_entry_cursor_map: dict[str, MockEntryCursor] = {}

        self._slug_match_list_map: dict[str, List[ModelMock]] = {}
        self._slug_match_entry_cursor_list_map: dict[str, List[MockEntryCursor]] = {}

        self.run_unmocked = False

        if mock_config_module_name is not None:
            self._load_configuration(mock_config_module_name)

    def reset(self):
        """
        Reset cursors so the mocks can be reused.
        """
        self._slug_entry_cursor_map.clear()
        self._slug_match_entry_cursor_list_map.clear()

    def _load_module_symbol(self, modulename, name):
        """ Import a named object from a module in the context of this function.
        """
        try:
            module = __import__(modulename, globals(), locals(), [name])
            value = vars(module)[name]
        except (ImportError, KeyError) as err:
            raise Exception(
                f'Error importing symbol {name} from module {modulename}: {err}')
        return value

    def _load_configuration(self, config_module_name: str):
        try:
            modulename, varname = os.path.splitext(config_module_name)
            if modulename and varname:
                config = self._load_module_symbol(modulename, varname[1:])
                self.add_mock_configuration(config)
        except Exception as exc:
            raise Exception(f'Error loading mocks mock module {config_module_name}: {exc}')

    def _split_output_match_list(self, slug: str, mocks: List[ModelMock]):
        output_list = []
        match_list = []
        for mock in mocks:
            if isinstance(mock, ModelMock):
                if mock.input:
                    match_list.append(mock)
                else:
                    output_list.append(mock)
            else:
                raise Exception(
                    f'Model mock value for slug {slug} '
                    'list must contain ModelMock instances.')

        return output_list, match_list

    def add_mock_configuration(self, config: ModelMockConfig):
        self.run_unmocked = config.run_unmocked

        models = config.models
        for slug, values in models.items():
            if isinstance(values, ModelMock):
                self._slug_entry_list_map[slug] = [values]
            elif isinstance(values, list):
                output_list, match_list = self._split_output_match_list(slug, values)
                if len(output_list) > 0:
                    self._slug_entry_list_map[slug] = output_list
                if len(match_list) > 0:
                    self._slug_match_list_map[slug] = match_list
            else:
                raise Exception(
                    f'Model mock value for slug {slug} must be a string, dict, list, or tuple.')

    def output_for_model(self, slug: str, input: dict) -> Union[dict, DTOType, str]:
        match_list = self._slug_match_list_map.get(slug)
        if match_list is not None:

            cursors = self._slug_match_entry_cursor_list_map.get(slug)
            if cursors is None:
                cursors = self._slug_match_entry_cursor_list_map[slug] = [
                    MockEntryCursor() for _m in match_list]

            for m, match in enumerate(match_list):
                # All items in the match_list will have the input option set
                cursor = cursors[m]
                output = cursor.next_output(match, input)
                if output is not None:
                    if isinstance(output, Exception):
                        raise output
                    return output

        outputs = self._slug_entry_list_map.get(slug)

        if outputs is not None:
            cursor = self._slug_entry_cursor_map.get(slug)
            if cursor is None:
                cursor = self._slug_entry_cursor_map[slug] = MockEntryCursor()

            output = cursor.next_output(outputs, input)

            if output is not None:
                if isinstance(output, Exception):
                    raise output
                return output

        if self.run_unmocked:
            return slug
        raise ModelMockException(f'No model mock for slug "{slug}" with input {input}')


def test():  # pylint: disable=too-many-branches,too-many-statements
    mock = ModelMockRunner()

    config = ModelMockConfig(
        models={
            "example.echo": ModelMock("example.echo"),
            "contrib.a": ModelMock({"a": 42}),
            "contrib.b": ModelMock([{"b": 1}, {"b": 2}, "contrib.b"]),
            "contrib.b-rep": ModelMock([{"b": 1}, {"b": 2},
                                        "contrib.b-rep"], repeat=2),
            "contrib.c": ModelMock({"c": 42}, input={"address": "0x00000000"}, repeat=2),
            "contrib.d": ModelMock([{"d": 1}, {"d": 2}],
                                   input={"address": "0x00000000"}),
            "contrib.e": [ModelMock({"e": 42}, input={"address": "0x00000000"}),
                          ModelMock({"e": 1})],
            "contrib.f": [ModelMock({"f": 42}, input={"address": "0x00000000"}),
                          ModelMock("contrib.f")],
            "contrib.g": ModelMock([ModelMock({"g": 1}, repeat=1),
                                    ModelMock({"g": 2}, repeat=2),
                                    ModelMock({"g": 3}, repeat=3)],
                                   repeat=2),
            "contrib.h": ModelMock(ModelDataError('Mock data error')),
            "contrib.i": ModelMock([ModelMock({"i": 1}, input={"x": 1}),
                                    ModelMock({"i": 2}, input={"x": 2}),
                                    ModelMock({"i": 3}, input={"x": 3})]),
        },
    )

    mock.add_mock_configuration(config)

    output = mock.output_for_model('example.echo', {})
    print(output)
    assert output == 'example.echo'

    output = mock.output_for_model('contrib.a', {})
    print(output)
    assert output == {"a": 42}

    for i in range(0, 10):
        output = mock.output_for_model('contrib.b', {})
        print(output)
        m = i % 3
        if m < 2:
            assert output == {'b': m + 1}
        else:
            assert output == 'contrib.b'

    for i in range(0, 8):
        try:
            output = mock.output_for_model('contrib.b-rep', {})
            print(output)
            assert i < 6
        except ModelMockException:
            assert i >= 6
            continue

        m = i % 3
        if m < 2:
            assert output == {'b': m + 1}
        else:
            assert output == 'contrib.b-rep'

    output = mock.output_for_model('contrib.c', {"address": "0x00000000", "symbol": "foo"})
    assert output == {"c": 42}
    output = mock.output_for_model('contrib.c', {"address": "0x00000000", "symbol": "foo"})
    assert output == {"c": 42}

    try:
        output = mock.output_for_model('contrib.c', {"address": "0x00000000", "symbol": "foo"})
        assert 'Repeat limit reached' == 'expected to raise'
    except ModelMockException:
        print('No output as expected.')

    try:
        output = mock.output_for_model('contrib.c', {"address": "0xffffffff", "symbol": "foo"})
        assert 'Input mismatch' == 'expected to raise'
    except ModelMockException:
        print('No input match as expected.')

    for i in range(0, 2):
        output = mock.output_for_model('contrib.d', {"address": "0x00000000", "symbol": "foo"})
        print(output)
        m = i % 2
        assert output == {'d': m + 1}

    output = mock.output_for_model('contrib.e', {"address": "0x00000000", "symbol": "foo"})
    assert output == {"e": 42}
    output = mock.output_for_model('contrib.e', {"address": "0xffffffff", "symbol": "foo"})
    assert output == {"e": 1}
    output = mock.output_for_model('contrib.f', {"address": "0x00000000", "symbol": "foo"})
    assert output == {"f": 42}
    output = mock.output_for_model('contrib.f', {"address": "0xffffffff", "symbol": "foo"})
    assert output == 'contrib.f'

    for i in range(0, 13):
        try:
            output = mock.output_for_model('contrib.g', {})
            print(output)
            assert i < 12
        except ModelMockException:
            assert i >= 12
            continue

        m = i % 6
        e = 1 if m == 0 else (2 if m in [1, 2] else 3)
        assert output == {'g': e}

    try:
        output = mock.output_for_model('contrib.h', {})
        assert "contrib.h" == "should raise an error"
    except ModelBaseError as err:
        print(err, 'as expected')

    output = mock.output_for_model('contrib.i', {"x": 2})
    print(output)
    assert output == {"i": 2}
    output = mock.output_for_model('contrib.i', {"x": 1})
    print(output)
    assert output == {"i": 1}
    output = mock.output_for_model('contrib.i', {"x": 1})
    print(output)
    assert output == {"i": 1}

    try:
        output = mock.output_for_model('contrib.i', {"x": 99})
        assert "contrib.i x=99" == "should raise an error"
    except ModelMockException as err:
        print(err, 'as expected')


if __name__ == '__main__':
    test()
