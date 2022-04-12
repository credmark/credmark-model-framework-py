# Error handling

When running a model, the top level framework code will catch any exceptions, convert it to a ModelRunError if needed, and output an error object in the response.

Models can raise a `ModelRunError` (or other Exception) to terminate a run.

When a model calls `self.context.run_model()` to run another model, an exception can be raised by the called model which will be received by the caller. `run_model()` can raise `ModelDataError`, `ModelRunError`, `ModelInputError`, `ModelNotFoundError` and various other sublasses of `ModelBaseError`.

The standard models are in `credmark.cmf.model.errors`.

In order for models to be consistently deterministic, the ONLY type of exception a model should catch and handle from a call to `run_model()` is a `ModelDataError`, which is considered a permanent error for the given context. All other errors are considered transient resource issues, coding errors, or conditions that may change in the future.

Because of this behavior, if a model raises a `ModelRunError` somewhere down a model run stack, the entire run will end up being aborted. This is by design.

## ModelBaseError

The `ModelBaseError` defines a set of properties that are common to all errors. The data associated with an error is available from an error instance at `error.data`. The following properties are available:

- `type` (string) Short identifying name for type of error

- `message` (string) A message about the error

- `code` (string) A short string, values to specific to the error type

- `detail` (object | null) - An object or null. Some errors may have a detail object containing error-specific data.

- `permanent` (boolean) If true the error is considered derministically permanent. This is currently only true for ModelDataErrors

- `stack` (list) The model run call stack. First element is the first called model and last element is the model that raised the error. An array of objects containing:

  - `slug` (string) Short identifying name for the model

  - `version` (string) Version of the model

  - `chainId` (number) Context chain id

  - `blockNumber` (number) Context block number

  - `trace` (string | null) Human-readable code trace that generated the error

## ModelDataError

A `ModelDataError` is an error that occurs during the lookup, generation, or processing of data this is considered deterministic and permanent, in the sense that for the given context, the same error will always occur.

A model may raise a ModelDataError in situations such as:

- the requested data does not exist or is not available for
  the current context block number.
- the input data is inconsistent, references non-existent
  items, or cannot be processed

A model may (and often should) catch and handle `ModelDataError`s raised from calls to `context.run_model()`.

Some standard `code`s have been defined for `ModelDataError`s, available at `ModelDataError.Codes`:

- `Codes.GENERIC = 'generic'` Default error code
- `Codes.NO_DATA = 'no_data'` Requested data does not exist (and never will for the given context)
- `Codes.CONFLICT = 'conflict'` There is an inherent conflict in the data for the given context that can never be resolved.

### Raising ModelDataError Errors

If you want your model to raise ModelDataError errors, you should add a `ModelDataErrorDesc` to the `errors` arg of your model `describe()` decorator with a description of the codes you are using and what they mean. For example:

```python
from credmark.cmf.model import Model, EmptyInput, ModelDataErrorDesc

@Model.describe(slug='example.data-error',
                         version='1.0',
                         display_name='Data Error Example',
                         description="A test model to generate a ModelDataError.",
                         input=EmptyInput,
                         errors=ModelDataErrorDesc(
                             code=ModelDataError.Codes.NO_DATA,
                             code_desc='Data does not exist'))
class ExampleModel(Model):
```

If you're using multiple codes, `ModelDataErrorDesc` also lets you pass in `codes` as a list of `(code, code_description)` tuples.

Then in your model `run()` code you simply raise a ModelDataError, for example:

```python
raise ModelDataError('Data does not exist', ModelDataError.Codes.NO_DATA)
```

## ModelInputError

If a model is using an input DTO, the expected model input parameters are automatically validated and a `ModelInputError` will be raised on error. `ModelInputError` is a non-permanent error because it's considered a coding error by the calling model.

The `ModelInputError` will contain a stack with the latest entry in the stack being the model that received the bad input data.

## Logging

Models should never write to stdout or use `print()`. They should use a logger to write to stderr. From a model, you can use `self.logger`.
