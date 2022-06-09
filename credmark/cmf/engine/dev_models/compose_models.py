from credmark.cmf.model import Model
from credmark.cmf.model.errors import ModelDataError
from credmark.cmf.types.compose import (MapBlockResult, MapBlockTimeSeries,
                                        MapBlockTimeSeriesInput, MapBlocksInput,
                                        MapBlocksOutput, MapInputsInput,
                                        MapInputsOutput, MapInputsResult)
from credmark.cmf.types.ledger import LedgerBlockNumberTimeSeries, LedgerBlockTimeSeriesInput


class LedgerModelSlugs:

    ledger_block_number_time_series = 'ledger.block-number-time-series'
    """
    Get a range of block numbers by end time, interval, and count
    """

# These models are local versions of models that are
# used during development with credmark-dev.
# Since these models call another model that might only exist
# locally, they need to run locally.


@Model.describe(slug='compose.map-block-time-series',
                version='0.0',
                display_name='Compose Map Block Time Series',
                description='Run a model on each of a time series of blocks',
                developer='Credmark',
                input=MapBlockTimeSeriesInput,
                output=MapBlockTimeSeries[dict])
class ComposeMapBlockTimeSeriesModel(Model):

    def run(self, input: MapBlockTimeSeriesInput) -> MapBlockTimeSeries[dict]:
        context = self.context

        ts_input = LedgerBlockTimeSeriesInput(
            endTimestamp=input.endTimestamp,
            interval=input.interval,
            count=input.count,
            exclusive=input.exclusive
        )

        block_series = context.run_model(LedgerModelSlugs.ledger_block_number_time_series,
                                         ts_input,
                                         return_type=LedgerBlockNumberTimeSeries)

        model_slug = input.modelSlug
        model_input = input.modelInput
        model_version = input.modelVersion

        if model_input is None:
            model_input = {}
        if model_version == '':
            model_version = None

        results = []

        for block_number in block_series.blockNumbers:
            try:
                run_output = context.run_model(
                    model_slug, model_input, block_number=block_number, version=model_version)

                row = MapBlockResult[dict](blockNumber=block_number,
                                           output=run_output)
            except ModelDataError as err:
                row = MapBlockResult[dict](blockNumber=block_number,
                                           error=err.data)

            results.append(row)

        return MapBlockTimeSeries[dict](endTimestamp=input.endTimestamp,
                                        interval=input.interval,
                                        exclusive=bool(input.exclusive),
                                        results=results)


@Model.describe(slug='compose.map-blocks',
                version='0.0',
                display_name='Compose Map Blocks',
                description='Run a model on each of a list of blocks',
                developer='Credmark',
                input=MapBlocksInput,
                output=MapBlocksOutput[dict])
class ComposeMapBlocksModel(Model):

    def run(self, input: MapBlocksInput) -> MapBlocksOutput[dict]:
        context = self.context

        model_slug = input.modelSlug
        model_input = input.modelInput
        model_version = input.modelVersion

        if model_input is None:
            model_input = {}
        if model_version == '':
            model_version = None

        results = []

        for block_number in input.blockNumbers:
            try:
                run_output = context.run_model(
                    model_slug, model_input, block_number=block_number, version=model_version)

                row = MapBlockResult[dict](blockNumber=block_number,
                                           output=run_output)
            except ModelDataError as err:
                row = MapBlockResult[dict](blockNumber=block_number,
                                           error=err.data)

            results.append(row)

        return MapBlocksOutput[dict](results=results)


@Model.describe(slug='compose.map-inputs',
                version='0.0',
                display_name='Compose Map Inputs',
                description='Run a model on each of a list of inputs',
                developer='Credmark',
                input=MapInputsInput,
                output=MapInputsOutput[dict, dict])
class ComposeMapInputsModel(Model):

    def run(self, input: MapInputsInput) -> MapInputsOutput[dict, dict]:
        context = self.context

        model_slug = input.modelSlug
        model_inputs = input.modelInputs
        model_version = input.modelVersion

        if model_version == '':
            model_version = None

        results = []

        for model_input in model_inputs:
            try:
                run_output = context.run_model(
                    model_slug, model_input, version=model_version)

                row = MapInputsResult(input=model_input,
                                      output=run_output)
            except ModelDataError as err:
                row = MapInputsResult(input=model_input,
                                      error=err.data)

            results.append(row)

        return MapInputsOutput[dict, dict](results=results)
