import datetime
from configparser import ConfigParser

from configuration.settings import DataCollectionRetrySettings, DataCollectionSettings

__all__ = ("ProgramConfiguration")


class ProgramConfiguration:
    """
    Represent configuration
    """
    def __init__(self, file_name: str) -> None:
        # classic ini file
        config = ConfigParser()
        config.read(file_name)

        self.__data_collection_settings = DataCollectionSettings(
            type=config["DATA_COLLECTION"]["TYPE"],
            contract=config["DATA_COLLECTION"]["CONTRACT"],
            date=datetime.date(
                year=int(config["DATA_COLLECTION"]["YEAR"]),
                month=int(config["DATA_COLLECTION"]["MONTH"]),
                day=int(config["DATA_COLLECTION"]["DAY"])
            )
        )

        self.__data_collection_retry_settings = DataCollectionRetrySettings(
            interval_sec=int(config["DATA_COLLECTION_SETTINGS"]["RETRY_INTERVAL_SEC"]),
            count=int(config["DATA_COLLECTION_SETTINGS"]["RETRY_INTERVAL_COUNT"]),
            delay_sec=int(config["DATA_COLLECTION_SETTINGS"]["DELAY_SEC"])
        )

    @property
    def data_collection_settings(self) -> DataCollectionSettings:
        return self.__data_collection_settings

    @property
    def data_collection_retry_settings(self) -> DataCollectionRetrySettings:
        return self.__data_collection_retry_settings
