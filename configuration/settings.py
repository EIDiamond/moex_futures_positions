from dataclasses import dataclass

__all__ = ("DataCollectionRetrySettings", "StorageSettings", "DataCollectionSettings")


@dataclass(eq=False, repr=True)
class DataCollectionSettings:
    type: str
    contract: str


@dataclass(eq=False, repr=True)
class DataCollectionRetrySettings:
    interval_sec: int
    count: int
    delay_sec: int


@dataclass(eq=False, repr=True)
class StorageSettings:
    root_path: str
