import datetime
import logging

from configuration.settings import StorageSettings
from data_collector.base_data_collector import IDataCollector
from data_reader.base_data_reader import IDataReader

__all__ = ("MOEXFuturesPositionsDataReader")

logger = logging.getLogger(__name__)


class MOEXFuturesPositionsDataReader(IDataReader):
    def __init__(
            self,
            moex_collector: IDataCollector,
            storage_settings: StorageSettings
    ):
        self.__moex_collector = moex_collector
        self.__storage_settings = storage_settings

    def read(self, date: datetime, contract: str) -> None:
        pass
