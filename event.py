from typing import Tuple
from pleasure_system import PleasureSignal


class Event:
    def __init__(self, description: str, need_dif: Tuple[float, float, float, float, float],
                 signal: PleasureSignal):
        self.description = description
        self.need_dif = need_dif
        self.pleasure_system_signal = signal
