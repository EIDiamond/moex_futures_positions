import datetime
import logging
from typing import Optional

import requests

from configuration.settings import DataCollectionRetrySettings
from data_collector.base_data_collector import IDataCollector
from position.position import OpenPositions, OpenPosition

__all__ = ("MOEXFuturesPositionsCollector")

logger = logging.getLogger(__name__)


class MOEXFuturesPositionsCollector(IDataCollector):
    def __init__(self, retry_settings: DataCollectionRetrySettings):
        self.__retry_settings = retry_settings

    def download(self, date: datetime.date, contract: str) -> Optional[OpenPositions]:
        try:
            r = requests.get(f"https://www.moex.com/api/contract/OpenOptionService/{date.day}.{date.month}.{date.year}/F/{contract}/json")

            logger.info(f"Status code: {r.status_code}")

            if r.status_code == 200:
                result = r.json()

                logger.info(f"Json result: {result}")
                """
                JSON FORMAT: 4 lines (list):
                0 - total count of open positions
                1 - total changes per day
                2 - total changes per day by percent
                3 - total count of clients
                """

                """ Different dates if day was not trading day (don't have any results) """
                if date.strftime("%d.%m.%Y") == result[0]["Date"]:
                    return OpenPositions(
                        contract=contract,
                        date=date,
                        positions=OpenPosition(
                            juridical_long=int(result[0]["JuridicalLong"].replace('\xa0', '')),
                            juridical_short=int(result[0]["JuridicalShort"].replace('\xa0', '')),
                            physical_long=int(result[0]["PhysicalLong"].replace('\xa0', '')),
                            physical_short=int(result[0]["PhysicalShort"].replace('\xa0', ''))
                        ),
                        clients=OpenPosition(
                            juridical_long=int(result[3]["JuridicalLong"].replace('\xa0', '')),
                            juridical_short=int(result[3]["JuridicalShort"].replace('\xa0', '')),
                            physical_long=int(result[3]["PhysicalLong"].replace('\xa0', '')),
                            physical_short=int(result[3]["PhysicalShort"].replace('\xa0', ''))
                        )
                    )
                else:
                    logger.info("Different dates was detected. Stop result parsing...")

        except Exception as ex:
            logger.error(f"Collect error has been occurred: {repr(ex)}")

        return None


