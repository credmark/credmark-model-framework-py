from datetime import datetime
from datetime import timedelta
from typing import Union


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
                             model_input: dict = {},
                             interval: str = None,
                             end_timestamp: int = None,
                             snap_clock: Union[str, None] = 'interval',
                             model_version: Union[str, None] = None) -> dict:
        (w_k, w_v) = self.parse_timerangestr(window)
        window_timestamp = self.range_timestamp(w_k, w_v)
        if interval is not None:
            (i_k, i_v) = self.parse_timerangestr(interval)
            interval_timestamp = self.range_timestamp(i_k, i_v)
            if snap_clock == 'interval':
                snap_clock = interval_timestamp
        else:
            interval_timestamp = self.range_timestamp(w_k, 1)
            if snap_clock == 'interval':
                snap_clock = w_k

        if snap_clock is None and end_timestamp is None:
            series_input = {
                "modelSlug": model_slug, 
                "modelInput": model_input,
                "modelVersion": model_version,
                "window": window_timestamp,
                "interval": interval_timestamp
            }
            return self.context.run_model('series.time-window-interval', series_input)
        else:
            
            if end_timestamp is None:
                end_timestamp = self.context.block_number.timestamp
            if snap_clock is not None:
                (s_k, s_v) = self.parse_timerangestr(snap_clock)
                snap_sec = self.range_timestamp(s_k, s_v)
                end_timestamp = end_timestamp - (end_timestamp % snap_sec)

            series_input = {
                "modelSlug": model_slug, 
                "modelInput": model_input,
                "modelVersion": model_version,
                "start": end_timestamp - window_timestamp,
                "end": end_timestamp,
                "interval": interval_timestamp
            }
            print(series_input)
            print(self.context.run_model('series.time-start-end-interval', series_input))
            return self.context.run_model('series.time-start-end-interval', series_input)

    def run_model_historical_blocks(self,
                             model_slug: str,
                             window: str,
                             model_input: dict = {},
                             interval: str = None,
                             end_timestamp: int = None,
                             snap_clock: Union[str, None] = 'interval',
                             model_version: Union[str, None] = None) -> dict:
        (w_k, w_v) = self.parse_timerangestr(window)
        window_timestamp = self.range_timestamp(w_k, w_v)
        if interval is not None:
            (i_k, i_v) = self.parse_timerangestr(interval)
            interval_timestamp = self.range_timestamp(i_k, i_v)
            if snap_clock == 'interval':
                snap_clock = interval_timestamp
        else:
            interval_timestamp = self.range_timestamp(w_k, 1)
            if snap_clock == 'interval':
                snap_clock = w_k

        if snap_clock is None and end_timestamp is None:
            series_input = {
                "modelSlug": model_slug, 
                "modelInput": model_input,
                "modelVersion": model_version,
                "window": window_timestamp,
                "interval": interval_timestamp
            }
            return self.context.run_model('series.time-window-interval', series_input)
        else:
            
            if end_timestamp is None:
                end_timestamp = self.context.block_number.timestamp
            if snap_clock is not None:
                (s_k, s_v) = self.parse_timerangestr(snap_clock)
                snap_sec = self.range_timestamp(s_k, s_v)
                end_timestamp = end_timestamp - (end_timestamp % snap_sec)

            series_input = {
                "modelSlug": model_slug, 
                "modelInput": model_input,
                "modelVersion": model_version,
                "start": end_timestamp - window_timestamp,
                "end": end_timestamp,
                "interval": interval_timestamp
            }
            print(series_input)
            print(self.context.run_model('series.time-start-end-interval', series_input))
            return self.context.run_model('series.time-start-end-interval', series_input)

    
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