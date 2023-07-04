from typing import Union

from credmark.cmf.model import CachePolicy, Model
from credmark.cmf.model.context import ModelContext
from credmark.cmf.model.errors import ModelDataError
from credmark.cmf.types.rpc import (
    RpcBlockRangeOutput,
    RpcBlockStartEndIntervalInput,
    RpcBlockWindowIntervalInput,
)
from credmark.cmf.types.series import (
    BlockSeries,
    BlockSeriesErrorRow,
    BlockSeriesRow,
    SeriesModelStartEndIntervalInput,
    SeriesModelWindowIntervalInput,
)
from credmark.dto import DTOType


class RpcModelSlugs:

    rpc_block_range_time_start_end_interval = 'rpc.get-block-range-time-start-end-interval'
    """
    Get a range of blocks by start and end time and interval
    """
    rpc_block_range_time_window_interval = 'rpc.get-block-range-time-window-interval'
    """
    Get a range of blocks by time window and interval
    """
    rpc_block_range_block_start_end_interval = 'rpc.get-block-range-block-start-end-interval'
    """
    Get a range of blocks by start and end block number and interval
    """
    rpc_block_range_block_window_interval = 'rpc.get-block-range-block-window-interval'
    """
    Get a range of blocks by block number window and interval
    """

# These models are local versions of models that are
# used during development with credmark-dev.
# Since these models call another model that might only exist
# locally, they need to run locally.


def run_model_for_block_range(context: ModelContext,
                              block_range: RpcBlockRangeOutput,
                              model_slug: str,
                              model_input: Union[DTOType, dict, None],
                              model_version: Union[str, None]):
    if model_input is None:
        model_input = {}
    if model_version == '':
        model_version = None

    block_series = BlockSeries[dict]()
    for block in block_range:
        block_number = block.blockNumber

        try:
            run_output = context.run_model(
                model_slug, model_input, block_number=block_number, version=model_version)

            row = BlockSeriesRow[dict](blockNumber=block_number,
                                       blockTimestamp=block.blockTimestamp,
                                       sampleTimestamp=block.sampleTimestamp,
                                       output=run_output)
            block_series.append(row)
        except ModelDataError as err:
            row = BlockSeriesErrorRow(blockNumber=block_number,
                                      blockTimestamp=block.blockTimestamp,
                                      sampleTimestamp=block.sampleTimestamp,
                                      error=err.data)
            block_series.append_error(row)

    return block_series


@Model.describe(slug='series.time-start-end-interval',
                version='0.0',
                display_name='Series Time Interval',
                description=('Run a model over a series of blocks specifying '
                             'a time start, end, and interval'),
                developer='Credmark',
                cache=CachePolicy.SKIP,
                input=SeriesModelStartEndIntervalInput,
                output=BlockSeries[dict])
class SeriesTimeStartEndInterval(Model):

    def run(self, input: SeriesModelStartEndIntervalInput) -> BlockSeries[dict]:
        rpc_input = RpcBlockStartEndIntervalInput(
            start=input.start,
            end=input.end,
            interval=input.interval
        )

        block_range = self.context.run_model(RpcModelSlugs.rpc_block_range_time_start_end_interval,
                                             rpc_input,
                                             return_type=RpcBlockRangeOutput)

        return run_model_for_block_range(self.context,
                                         block_range,
                                         input.modelSlug,
                                         input.modelInput,
                                         input.modelVersion)


@Model.describe(slug='series.time-window-interval',
                version='0.0',
                display_name='Series Time Window Interval',
                description='Run a model over a series of blocks specifying '
                'a time window and interval',
                developer='Credmark',
                cache=CachePolicy.SKIP,
                input=SeriesModelWindowIntervalInput,
                output=BlockSeries[dict])
class SeriesTimeWindowInterval(Model):

    def run(self, input: SeriesModelWindowIntervalInput) -> BlockSeries[dict]:
        rpc_input = RpcBlockWindowIntervalInput(
            window=input.window,
            interval=input.interval
        )

        block_range = self.context.run_model(RpcModelSlugs.rpc_block_range_time_window_interval,
                                             rpc_input,
                                             return_type=RpcBlockRangeOutput)

        return run_model_for_block_range(self.context,
                                         block_range,
                                         input.modelSlug,
                                         input.modelInput,
                                         input.modelVersion)


@Model.describe(slug='series.block-start-end-interval',
                version='0.0',
                display_name='Series Block Interval',
                description='Run a model over a series of blocks specifying '
                'a block start, end, and interval',
                developer='Credmark',
                cache=CachePolicy.SKIP,
                input=SeriesModelStartEndIntervalInput,
                output=BlockSeries[dict])
class SeriesBlockStartEndInterval(Model):

    def run(self, input: SeriesModelStartEndIntervalInput) -> BlockSeries[dict]:
        rpc_input = RpcBlockStartEndIntervalInput(
            start=input.start,
            end=input.end,
            interval=input.interval
        )

        block_range = self.context.run_model(RpcModelSlugs.rpc_block_range_block_start_end_interval,
                                             rpc_input,
                                             return_type=RpcBlockRangeOutput)

        return run_model_for_block_range(self.context,
                                         block_range,
                                         input.modelSlug,
                                         input.modelInput,
                                         input.modelVersion)


@Model.describe(slug='series.block-window-interval',
                version='0.0',
                display_name='Series Block Window Interval',
                description='Run a model over a series of blocks specifying '
                'a block window and interval',
                developer='Credmark',
                cache=CachePolicy.SKIP,
                input=SeriesModelWindowIntervalInput,
                output=BlockSeries[dict])
class SeriesBlockWindowInterval(Model):

    def run(self, input: SeriesModelWindowIntervalInput) -> BlockSeries[dict]:
        rpc_input = RpcBlockWindowIntervalInput(
            window=input.window,
            interval=input.interval
        )

        block_range = self.context.run_model(RpcModelSlugs.rpc_block_range_block_window_interval,
                                             rpc_input,
                                             return_type=RpcBlockRangeOutput)

        return run_model_for_block_range(self.context,
                                         block_range,
                                         input.modelSlug,
                                         input.modelInput,
                                         input.modelVersion)
