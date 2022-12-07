import abc
import datetime

from position.position import OpenPositions

__all__ = ("IDataCollector")


class IDataCollector(abc.ABC):
    @abc.abstractmethod
    def download(self, date: datetime.date, contract: str) -> OpenPositions:
        pass
