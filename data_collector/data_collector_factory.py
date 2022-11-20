from typing import Optional

from data_collector.base_data_collector import IDataCollector
from data_collector.moex.moex_futures_open_positions import MOEXFuturesPositionsCollector

__all__ = ("DataCollectorFactory")


class DataCollectorFactory:
    """
    Fabric for collectors. Put here a new collector class.
    """
    @staticmethod
    def new_factory(collector_type: str, *args, **kwargs) -> Optional[IDataCollector]:
        match collector_type:
            case "moex_futures_open_positions":
                return MOEXFuturesPositionsCollector(*args, **kwargs)
            case _:
                return None
