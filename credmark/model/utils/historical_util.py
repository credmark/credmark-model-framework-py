from typing import (
    Type,
    TypeVar,
    Union,
    List,
)
import credmark.model
from credmark.model.errors import ModelRunError
from credmark.types import (
    BlockSeries,
    SeriesModelStartEndIntervalInput,
    SeriesModelWindowIntervalInput,
)
from credmark.types.dto import DTO

DTOCLS = TypeVar('DTOCLS')


class HistoricalUtil:

    time_units = [
        'year',
        'month',
        'week',
        'day',
        'hour',
        'minute',
        'second'
    ]

    time_unit_seconds = {
        'year': 365 * 24 * 60 * 60,
        'month': 30 * 24 * 60 * 60,
        'week': 7 * 24 * 60 * 60,
        'day': 24 * 60 * 60,
        'hour': 60 * 60,
        'minute': 60,
        'second': 1,
    }

    def __init__(self, context) -> None:
        self.context: credmark.model.ModelContext = context

    def run_model_historical(self,
                             model_slug: str,
                             window: Union[str, List[str]],
                             model_input: Union[dict, DTO, None] = None,
                             interval: Union[str, None] = None,
                             end_timestamp: Union[int, None] = None,
                             snap_clock: Union[str, None] = 'interval',
                             model_return_type: Type[DTOCLS] = dict,
                             model_version: Union[str, None] = None) -> BlockSeries[DTOCLS]:
        """
        Run a model over a series of historical blocks.

        :param model_slug: the slug of the model to run
        :param window: a string defining a time window, ex. "30 day"
        :param interval: a string defining a time interval, ex. "1 day", or list of time intervals to be summed.
        :param model_input: input passed to the model being run
        :param model_return_type: the DTO class or dict for the output of the model
             being run. This will be the type of the BlockSeriesRow.output
        """
        if model_version is None:
            model_version = ''
        if model_input is None:
            model_input = {}
        run_return_type = BlockSeries[model_return_type]

        if isinstance(window, list):
            parsed_window = [self.range_timestamp(*self.parse_timerangestr(w)) for w in window]
            min_w = window[parsed_window.index(min(parsed_window))]
            (w_k, _) = self.parse_timerangestr(min_w)
            window_timestamp = sum(parsed_window)
        else:
            (w_k, w_v) = self.parse_timerangestr(window)
            window_timestamp = self.range_timestamp(w_k, w_v)
        if window_timestamp <= 0:
            raise ModelRunError(
                f"Negative or zero window '{window}' specified for historical.")

        if interval is not None:
            (i_k, i_v) = self.parse_timerangestr(interval)
            interval_timestamp = self.range_timestamp(i_k, i_v)
        else:
            interval_timestamp = self.range_timestamp(w_k, 1)
        if interval_timestamp <= 0:
            raise ModelRunError(
                f"Negative or zero interval '{interval}' specified for historical.")

        if snap_clock is None and end_timestamp is None:

            input = SeriesModelWindowIntervalInput(
                modelSlug=model_slug,
                modelInput=model_input,
                modelVersion=model_version,
                window=window_timestamp,
                interval=interval_timestamp
            )
            return self.context.run_model('series.time-window-interval',
                                          input,
                                          return_type=run_return_type)  # type: ignore
        else:

            if end_timestamp is None:
                end_timestamp = self.context.block_number.timestamp
            if snap_clock is not None:
                if snap_clock == 'interval':
                    snap_sec = interval_timestamp
                else:
                    (s_k, s_v) = self.parse_timerangestr(snap_clock)
                    snap_sec = self.range_timestamp(s_k, s_v)

                end_timestamp = end_timestamp - (end_timestamp % snap_sec)

            input = SeriesModelStartEndIntervalInput(
                modelSlug=model_slug,
                modelInput=model_input,
                modelVersion=model_version,
                start=end_timestamp - window_timestamp,
                end=end_timestamp,
                interval=interval_timestamp
            )

            return self.context.run_model('series.time-start-end-interval',
                                          input,
                                          return_type=run_return_type)  # type: ignore

    def run_model_historical_blocks(self,
                                    model_slug: str,
                                    window: int,
                                    interval: int,
                                    model_input: Union[dict, DTO, None] = None,
                                    end_block: Union[int, None] = None,
                                    snap_block: Union[int, None] = None,
                                    model_return_type: Type[DTOCLS] = dict,
                                    model_version: Union[str, None] = None) -> BlockSeries[DTOCLS]:
        """
        Run a model over a series of historical blocks.

        :param model_slug: the slug of the model to run
        :param window: number of blocks
        :param interval: number of blocks for each interval
        :param model_input: input passed to the model being run
        :param model_return_type: the DTO class or dict for the output of the model
             being run. This will be the type of the BlockSeriesRow.output
        """
        if model_version is None:
            model_version = ''
        if model_input is None:
            model_input = {}
        run_return_type = BlockSeries[model_return_type]

        if snap_block is None and end_block is None:
            series_input = SeriesModelWindowIntervalInput(
                modelSlug=model_slug,
                modelInput=model_input,
                modelVersion=model_version,
                window=window,
                interval=interval
            )
            return self.context.run_model('series.block-window-interval',
                                          series_input,
                                          return_type=run_return_type)  # type: ignore
        else:
            if end_block is None:
                end_block = self.context.block_number
            if snap_block is not None:
                end_block = end_block - (end_block % snap_block)

            series_input = SeriesModelStartEndIntervalInput(
                modelSlug=model_slug,
                modelInput=model_input,
                modelVersion=model_version,
                start=end_block - window,
                end=end_block,
                interval=interval
            )
            return self.context.run_model('series.block-start-end-interval',
                                          series_input,
                                          return_type=run_return_type)  # type: ignore

    def parse_timerangestr(self, time_str: str):
        key = None

        for unit in self.time_units:
            if unit in time_str:
                key = unit

        if key is None:
            raise ModelRunError(
                f"Invalid historical time string '{time_str}': "
                f"unit not one of {','.join(self.time_units)}")

        try:
            num = int(time_str.split(' ')[0])
        except Exception as err:
            raise ModelRunError(
                f"Invalid historical time string '{time_str}': "
                f"unknown number format")
        return (key, num)

    def range_timestamp(self, key: str, num: int):
        return self.time_unit_seconds[key] * num
