from typing import Union
import credmark.model
from credmark.model.context import ModelContext
from credmark.types import BlockSeries, BlockSeriesRow, \
    SeriesModelStartEndIntervalInput, SeriesModelWindowIntervalInput
from credmark.types.models.core import CoreModels
from credmark.types.models.rpc import RpcBlockRangeOutput, \
    RpcBlockStartEndIntervalInput, RpcBlockWindowIntervalInput
from credmark.dto import DTO

# These models are local versions of models that are
# used during development. They have high version numbers
# so they take priority over versions on the server.


def run_model_for_block_range(context: ModelContext,
                              block_range: RpcBlockRangeOutput,
                              model_slug: str,
                              model_input: Union[DTO, dict, None],
                              model_version: Union[str, None]):
    block_series = BlockSeries[dict]()
    for block in block_range:
        block_number = block.blockNumber
        if model_input is None:
            model_input = {}

        run_output = context.run_model(
            model_slug, model_input, block_number=block_number, version=model_version)

        row = BlockSeriesRow[dict](blockNumber=block_number,
                                   blockTimestamp=block.blockTimestamp,
                                   sampleTimestamp=block.sampleTimestamp,
                                   output=run_output)
        block_series.append(row)

    return block_series


@credmark.model.describe(slug='series.time-start-end-interval',
                         version='100.0',
                         display_name='Series Time Interval',
                         description='Run a model over a series of blocks specifying a time start, end, and interval',
                         developer='Credmark',
                         input=SeriesModelStartEndIntervalInput,
                         output=BlockSeries[dict])
class SeriesTimeStartEndInterval(credmark.model.Model):

    def run(self, input: SeriesModelStartEndIntervalInput) -> BlockSeries[dict]:
        rpc_input = RpcBlockStartEndIntervalInput(
            start=input.start,
            end=input.end,
            interval=input.interval
        )

        block_range = self.context.run_model(CoreModels.rpc_block_range_time_start_end_interval,
                                             rpc_input,
                                             return_type=RpcBlockRangeOutput)

        return run_model_for_block_range(self.context,
                                         block_range,
                                         input.modelSlug,
                                         input.modelInput,
                                         input.modelVersion)


@credmark.model.describe(slug='series.time-window-interval',
                         version='100.0',
                         display_name='Series Time Window Interval',
                         description='Run a model over a series of blocks specifying a time window and interval',
                         developer='Credmark',
                         input=SeriesModelWindowIntervalInput,
                         output=BlockSeries[dict])
class SeriesTimeWindowInterval(credmark.model.Model):

    def run(self, input: SeriesModelWindowIntervalInput) -> BlockSeries[dict]:
        rpc_input = RpcBlockWindowIntervalInput(
            window=input.window,
            interval=input.interval
        )

        block_range = self.context.run_model(CoreModels.rpc_block_range_time_window_interval,
                                             rpc_input,
                                             return_type=RpcBlockRangeOutput)

        return run_model_for_block_range(self.context,
                                         block_range,
                                         input.modelSlug,
                                         input.modelInput,
                                         input.modelVersion)


@credmark.model.describe(slug='series.block-start-end-interval',
                         version='100.0',
                         display_name='Series Block Interval',
                         description='Run a model over a series of blocks specifying a block start, end, and interval',
                         developer='Credmark',
                         input=SeriesModelStartEndIntervalInput,
                         output=BlockSeries[dict])
class SeriesBlockStartEndInterval(credmark.model.Model):

    def run(self, input: SeriesModelStartEndIntervalInput) -> BlockSeries[dict]:
        rpc_input = RpcBlockStartEndIntervalInput(
            start=input.start,
            end=input.end,
            interval=input.interval
        )

        block_range = self.context.run_model(CoreModels.rpc_block_range_block_start_end_interval,
                                             rpc_input,
                                             return_type=RpcBlockRangeOutput)

        return run_model_for_block_range(self.context,
                                         block_range,
                                         input.modelSlug,
                                         input.modelInput,
                                         input.modelVersion)


@credmark.model.describe(slug='series.block-window-interval',
                         version='100.0',
                         display_name='Series Block Window Interval',
                         description='Run a model over a series of blocks specifying a block window and interval',
                         developer='Credmark',
                         input=SeriesModelWindowIntervalInput,
                         output=BlockSeries[dict])
class SeriesBlockWindowInterval(credmark.model.Model):

    def run(self, input: SeriesModelWindowIntervalInput) -> BlockSeries[dict]:
        rpc_input = RpcBlockWindowIntervalInput(
            window=input.window,
            interval=input.interval
        )

        block_range = self.context.run_model(CoreModels.rpc_block_range_block_window_interval,
                                             rpc_input,
                                             return_type=RpcBlockRangeOutput)

        return run_model_for_block_range(self.context,
                                         block_range,
                                         input.modelSlug,
                                         input.modelInput,
                                         input.modelVersion)
