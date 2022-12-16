import abc
import datetime
from typing import Generator

from position.position import OpenPositions

__all__ = ("IDataCollector")


class IDataCollector(abc.ABC):
    @abc.abstractmethod
    def download(
            self,
            date: datetime.date,
            contract: str
    ) -> OpenPositions:
        pass

    @abc.abstractmethod
    def download_range(
            self,
            date: datetime.date,
            contract: str,
            days_range: int
    ) -> Generator[OpenPositions, None, None]:
        pass
