from datetime import datetime
from datetime import timedelta
from typing import Union


from ..types import BlockSeriesDTO, SeriesModelInput
from ..types.dto import DTO


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
        'month':  30 * 24 * 60 * 60,
        'week':  7 * 24 * 60 * 60,
        'day':   24 * 60 * 60,
        'hour':   60 * 60,
        'minute':  60,
        'second':  1,
    }

    def __init__(self, context) -> None:
        self.context = context

    def run_model_historical(self,
                             model_slug: str,
                             window: str,
                             model_input: Union[dict, DTO] = {},
                             interval: str = None,
                             end_timestamp: int = None,
                             snap_clock: Union[str, None] = 'interval',
                             model_version: Union[str, None] = None) -> BlockSeriesDTO:
        (w_k, w_v) = self.parse_timerangestr(window)
        window_timestamp = self.range_timestamp(w_k, w_v)
        if interval is not None:
            (i_k, i_v) = self.parse_timerangestr(interval)
            interval_timestamp = self.range_timestamp(i_k, i_v)
        else:
            interval_timestamp = self.range_timestamp(w_k, 1)

        if snap_clock is None and end_timestamp is None:
            
            input = SeriesModelInput(**{
                "modelSlug": model_slug, 
                "modelInput": model_input,
                "modelVersion": model_version,
                "window": window_timestamp,
                "interval": interval_timestamp
            })
            return self.context.run_model('series.time-window-interval', input,return_type=BlockSeriesDTO)
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
            
            input = SeriesModelInput(
                modelSlug= model_slug, 
                modelInput= model_input,
                modelVersion= model_version,
                start= end_timestamp - window_timestamp,
                end= end_timestamp,
                interval= interval_timestamp
            )
            
            return self.context.run_model('series.time-start-end-interval', input, return_type=BlockSeriesDTO)

    def run_model_historical_blocks(self,
                             model_slug: str,
                             window: int,
                             interval: int,
                             model_input: dict = {},
                             end_block: Union[int, None] = None,
                             snap_block: Union[int, None] = None,
                             model_version: Union[str, None] = None) -> BlockSeriesDTO:

        if snap_block is None and end_block is None:
            series_input = {
                "modelSlug": model_slug, 
                "modelInput": model_input,
                "modelVersion": model_version,
                "window": window,
                "interval": interval
            }
            return self.context.run_model('series.block-window-interval', series_input, return_type=BlockSeriesDTO)
        else:
            if end_block is None:
                end_block = self.context.block_number
            if snap_block is not None:
                end_block = end_block - (end_block % snap_block)

            series_input = {
                "modelSlug": model_slug, 
                "modelInput": model_input,
                "modelVersion": model_version,
                "start": end_block - window,
                "end": end_block,
                "interval": interval
            }
            return self.context.run_model('series.block-start-end-interval', series_input, return_type=BlockSeriesDTO)

    
    def parse_timerangestr(self, time_str: str):
        for unit in self.time_units:
            if unit in time_str:
                key = unit
        try:
            num = int(time_str.split(' ')[0])
            if num <= 0:
                num = 1
        except:
            num = 1

        return (key, num)
    
    def range_timestamp(self, key: str, num: int):
        return self.time_unit_seconds[key] * num