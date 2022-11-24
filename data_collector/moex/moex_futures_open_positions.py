import datetime
import logging

from configuration.settings import DataCollectionRetrySettings
from data_collector.base_data_collector import IDataCollector

__all__ = ("MOEXFuturesPositionsCollector")

logger = logging.getLogger(__name__)


class MOEXFuturesPositionsCollector(IDataCollector):
    def __init__(self, retry_settings: DataCollectionRetrySettings):
        self.__retry_settings = retry_settings

    def download(self, date: datetime, contract: str) -> None:
        pass
