from typing import Union
import credmark.model
from credmark.model.context import ModelContext
from credmark.types import BlockSeries, BlockSeriesRow, \
    SeriesModelStartEndIntervalInput, SeriesModelWindowIntervalInput
from credmark.types.models.core import CoreModels
from credmark.types.models.rpc import RpcBlockRangeOutput, \
    RpcBlockStartEndIntervalInput, RpcBlockWindowIntervalInput
from credmark.types.dto import DTO

# This models are local versions of models that are
# used during development.


def run_model_for_block_range(context: ModelContext,
                              block_range: RpcBlockRangeOutput,
                              model_slug: str,
                              model_input: Union[DTO, dict, None],
                              model_version: Union[str, None]):
    block_series = BlockSeries[dict]()
    for block_num in block_range:
        run_output = context.run_model(
            model_slug, model_input, version=model_version)

        row = BlockSeriesRow[dict](blockNumber=block_num.blockNumber,
                                   blockTimestamp=block_num.blockTimestamp,
                                   sampleTimestamp=block_num.sampleTimestamp,
                                   output=run_output)
        block_series.append(row)

    return block_series


@credmark.model.describe(slug='series.time-start-end-interval',
                         version='1.0',
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
                         version='1.0',
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
                         version='1.0',
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
                         version='1.0',
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
