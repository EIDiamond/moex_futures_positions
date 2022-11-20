import datetime
import logging

from data_collector.base_data_collector import IDataCollector

__all__ = ("CSVDataStorage")

logger = logging.getLogger(__name__)


class MOEXFuturesPositionsCollector(IDataCollector):
    def download(self, date: datetime, contract: str) -> None:
        pass
