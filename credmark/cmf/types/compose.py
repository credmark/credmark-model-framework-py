from datetime import datetime
from typing import Callable, Generic, List, Optional, Tuple, TypeVar, Union

import pandas as pd
from credmark.cmf.model.errors import ModelErrorDTO
from credmark.dto import (DTO, DTOField, DTOType, GenericDTO,
                          IterableListGenericDTO, PrivateAttr)

from .block_number import BlockNumber

DTOCLS = TypeVar('DTOCLS')
INPUTDTOCLS = TypeVar('INPUTDTOCLS')


class MapInputsResult(GenericDTO, Generic[INPUTDTOCLS, DTOCLS]):
    """
    A data row in an input series.
    The generic type specifies the classes to use as the input and output.

    For example ``row = MapInputResult[MyInputClass, MyOutputClass](**data)``
    where ``row.input`` will be an instance of ``MyInputClass``
    and ``row.output`` will be an instance of ``MyOutputClass``
    """
    input: Union[INPUTDTOCLS, dict] = DTOField(
        description='Input used for the run.')
    output: Union[DTOCLS, None] = DTOField(
        default=None,
        description='Model output of result. Will not be present if there is an error.')
    error: Union[ModelErrorDTO, None] = DTOField(
        default=None,
        description='Error DTO from model run. Will not be present if output exists.')

    class Config:
        schema_extra = {
            'examples': [{'input': {'address': '0xC18360217D8F7Ab5e7c516566761Ea12Ce7F9D72'},
                          'output': {'result': 42},
                          'error': None}]
        }


class MapInputsOutput(IterableListGenericDTO[MapInputsResult[INPUTDTOCLS, DTOCLS]],
                      Generic[INPUTDTOCLS, DTOCLS]):
    """
    A DTO for the output of "compose.map-inputs" model which runs another
    model over a list of inputs.

    The generic types specify the classes to use as the input and output
    in the ``MapInputsResult``.

    For example ``map_result = MapInputsOutput[MyInputClass, MyOutputClass](**data)``
    where ``map_result.results[0].input`` will be an instance of ``MyInputClass``
    where ``map_result.result[0].output`` will be an instance of ``MyOutputClass``

    If a permanent error occurs during a model run, the block with error
    will be added to the series array.
    If a non-permanent error occurs during a model run, the entire series
    will generate an error.

    The output can be converted to list (to_list) or Panda's DataFrame (to_dataframe())
    with customized lambdas to extract certain field(s) of the output into
    values (in a list) or columns (in a dataframe).
    """
    results: List[MapInputsResult[INPUTDTOCLS, DTOCLS]] = DTOField(
        default=[], description='List of model run results')
    _iterator: str = PrivateAttr('results')

    class Config:
        schema_extra = {
            'examples': [{'results': ex}
                         for ex in
                         MapInputsResult[INPUTDTOCLS, DTOCLS].Config.schema_extra['examples']]
        }

    def to_list(self, fields: Optional[List[Callable]] = None) -> List[List]:
        """
        Parameters:
            fields (List[Callable] | None): List of lambda to extract certain field from output.
                Leave empty to extract the entire output.
        Extract tuples from results data
        """
        if fields is None:
            return [[p.input,
                    p.output,
                    p.error]
                    for p in self.results]
        else:
            return [[p.input, *[f(p.output) for f in fields], p.error]
                    for p in self.results]

    def to_dataframe(self, fields: Optional[List[Tuple[str, Callable]]] = None) -> pd.DataFrame:
        """
        Parameters:
            fields (List[Tuple[str, Callable]] | None): List of field name and lambda to extract
                certain field from output. Leave empty to extract the entire output.
        Extract tuples from results data

        """
        results_as_list = self.to_list(
            fields=None if fields is None else [f for (_, f) in fields])
        if fields is None:
            return pd.DataFrame(results_as_list, columns=['input', 'output', 'error'])
        else:
            return pd.DataFrame(results_as_list,
                                columns=['input'] + [c for c, _ in fields] + ['error'])


class MapBlockResult(GenericDTO, Generic[DTOCLS]):
    """
    A data row in a block series.
    The generic type specifies the class to use as the output.

    For example ``row = MapBlockResult[MyOutputClass](**data)``
    where ``row.output`` will be an instance of ``MyOutputClass``.
    """

    blockNumber: BlockNumber = DTOField(
        description='Block number of result.')
    output: Union[DTOCLS, None] = DTOField(
        default=None,
        description='Model output of result. Will not be present if there is an error.')
    error: Union[ModelErrorDTO, None] = DTOField(
        default=None,
        description='Error DTO from model run. Will not be present if output exists.')


class MapBlocksOutput(IterableListGenericDTO[MapBlockResult[DTOCLS]], Generic[DTOCLS]):
    """
    A DTO for the output of ``compose.map-*`` block models which run another
    model over a series of blocks.

    The generic type specifies the class to use as the output
    in the ``MapBlockResult``.

    For example ``block_results = BlockSeries[MyOutputClass](**data)``
    where ``block_results.results[0].output`` will be an instance of ``MyOutputClass``

    If a permanent error occurs during a model run, the block with error
    will be added to the series array.
    If a non-permanent error occurs during a model run, the entire series
    will generate an error.

    The output can be converted to list (to_list) or Panda's DataFrame (to_dataframe())
    with customized lambdas to extract certain field(s) of the output into
    values (in a list) or columns (in a dataframe).
    """

    results: List[MapBlockResult[DTOCLS]] = DTOField(
        default=[], description='List of results of block model run outputs')
    _iterator: str = PrivateAttr('results')

    def get(self, block_number=None, timestamp=None) -> Union[MapBlockResult[DTOCLS], None]:
        if block_number is not None:
            return next((x for x in self.results if x.blockNumber == block_number), None)
        if timestamp is not None:
            return self.get(
                block_number=max(s.blockNumber for s in
                                 [s for s in self.results
                                  if s.blockNumber.timestamp <= timestamp]))
        return None

    def to_list(self, fields: Optional[List[Callable]] = None) -> List[List]:
        """
        Parameters:
            fields (List[Callable] | None): List of lambda to extract certain field from output.
                Leave empty to extract the entire output.
        Extract tuples from results data
        """
        if fields is None:
            return [[p.blockNumber,
                    datetime.utcfromtimestamp(p.blockNumber.timestamp),
                    p.output,
                    p.error]
                    for p in self.results]
        else:
            return [([p.blockNumber,
                    datetime.utcfromtimestamp(p.blockNumber.timestamp)] +
                    [f(p.output) for f in fields] +
                    [p.error])
                    for p in self.results]

    def to_dataframe(self, fields: Optional[List[Tuple[str, Callable]]] = None) -> pd.DataFrame:
        """
        Parameters:
            fields (List[Tuple[str, Callable]] | None): List of field name and lambda to extract
                certain field from output. Leave empty to extract the entire output.
        Extract tuples from results data

        """
        results_as_list = self.to_list(fields=None if fields is None else [
                                       f for (_, f) in fields])
        if fields is None:
            return pd.DataFrame(results_as_list,
                                columns=['blockNumber', 'blockTime', 'output', 'error'])
        else:
            return pd.DataFrame(results_as_list,
                                columns=(['blockNumber', 'blockTime'] +
                                         [c for c, _ in fields] +
                                         ['error']))


class MapBlockTimeSeriesOutput(MapBlocksOutput[DTOCLS], Generic[DTOCLS]):
    """
    Output for the compose.map-block-time-series model.
    """
    endTimestamp: int = DTOField(
        ...,
        description='End timestamp of block series, inclusive unless exclusive is True.')
    interval: int = DTOField(...,
                             description='Interval in seconds of the sample timestamp.')
    exclusive: bool = DTOField(...,
                               description='If true, blocks are exclusive of end timestamp.')


class MapBlockTimeSeriesInput(DTO):
    """
    Input for the compose.map-block-time-series model.
    """
    endTimestamp: int = DTOField(
        description='End timestamp of block series, inclusive unless exclusive is True')
    interval: int = DTOField(description='Series interval in seconds')
    count: int = DTOField(description='Number of intervals in the series.')
    exclusive: Union[bool, None] = DTOField(
        default=False, description='If true, blocks are exclusive of end timestamp')
    modelInput: Union[dict, DTOType, None] = DTOField(
        default=None,
        description='Input for the model run at each block number.')
    modelSlug: str = DTOField(
        description='Slug of model to run at each block number.')
    modelVersion: Optional[str] = DTOField(
        default=None,
        description='Optional version of the model to run. Normally you should not set this.')


class MapInputsInput(DTO):
    """
    Input for the compose.map-inputs model.
    """
    modelInputs: List[Union[dict, DTOType]] = DTOField(
        description='A list of inputs. The specified model will be run once with each input.')
    modelSlug: str = DTOField(
        description='Slug of model to run with each input.')
    modelVersion: Optional[str] = DTOField(
        default=None,
        description='Optional version of the model to run. Normally you should not set this.')


class MapBlocksInput(DTO):
    """
    Input for the compose.map-blocks model.
    """
    blockNumbers: List[BlockNumber] = DTOField(
        description='List of block numbers. The specified model will be run for each block number.'
    )
    modelInput: Union[dict, DTOType, None] = DTOField(
        default=None,
        description='Input for the model run at each block number.')
    modelSlug: str = DTOField(
        description='Slug of model to run at each block number.')
    modelVersion: Optional[str] = DTOField(
        default=None,
        description='Optional version of the model to run. Normally you should not set this.')
