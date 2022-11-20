import abc
import datetime

__all__ = ("IDataCollector")


class IDataCollector(abc.ABC):
    @abc.abstractmethod
    def download(self, date: datetime, contract: str) -> None:
        pass
