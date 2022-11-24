import datetime
import logging
from pathlib import Path

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
        """
        Lazy data load from moex api server.
        """
        root_dir = Path(self.__storage_settings.root_path)
        MOEXFuturesPositionsDataReader.__check_or_mk_dir(root_dir)

        contract_file = Path(
            root_dir,
            f"{contract}-{str(date.year)}-{str(date.month)}-{str(date.day)}.csv"
        )

        if contract_file.exists():
            pass
        else:
            pass

    @staticmethod
    def __check_or_mk_dir(directory: Path) -> Path:
        if not directory.exists():
            logger.info(f"Directory doesn't exist: {directory}. Making...")
            directory.mkdir()

        return directory
