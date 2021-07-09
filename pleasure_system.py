from needs import *
from dataclasses import dataclass
from typing import Tuple, Type


@dataclass
class PleasureSignal:
    pleasure_signal: bool
    need: Type[Need]
    location: Tuple[float, float] or None


@dataclass
class EventSchemata:
    """
    Event schemata helps PSI predict the results of certain actions.
    """
    associated_signals: Tuple[PleasureSignal]
    description: str

