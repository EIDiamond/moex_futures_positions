import datetime
from dataclasses import dataclass

__all__ = ("OpenPositions")


@dataclass(eq=False, repr=True)
class OpenPosition:
    juridical_long: int
    juridical_short: int
    physical_long: int
    physical_short: int


@dataclass(eq=False, repr=True)
class OpenPositions:
    contract: str
    date: datetime.date
    positions: OpenPosition
    clients: OpenPosition
