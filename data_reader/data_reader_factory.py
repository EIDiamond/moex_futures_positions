from typing import Optional

from data_reader.base_data_reader import IDataReader
from data_reader.csv_or_api.csv_or_api_data import MOEXFuturesPositionsDataReader

__all__ = ("DataReaderFactory")


class DataReaderFactory:
    @staticmethod
    def new_factory(*args, **kwargs) -> Optional[IDataReader]:
        return MOEXFuturesPositionsDataReader(*args, **kwargs)
