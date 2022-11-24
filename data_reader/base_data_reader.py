import abc
import datetime

__all__ = ("IDataReader")


class IDataReader(abc.ABC):
    @abc.abstractmethod
    def read(self, date: datetime, contract: str) -> None:
        pass
