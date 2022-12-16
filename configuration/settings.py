import datetime
from dataclasses import dataclass

__all__ = ("DataCollectionRetrySettings", "DataCollectionSettings")


@dataclass(eq=False, repr=True)
class DataCollectionSettings:
    type: str
    contract: str
    date:  datetime.date
    days_range: int


@dataclass(eq=False, repr=True)
class DataCollectionRetrySettings:
    interval_sec: int
    count: int
    delay_between_days_sec: int
