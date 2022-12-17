import datetime
from configparser import ConfigParser

from configuration.settings import DataCollectionRetrySettings, DataCollectionSettings, DataStorageSettings

__all__ = ("ProgramConfiguration")


class ProgramConfiguration:
    """
    Represent configuration
    """
    def __init__(
            self,
            configuration_file_name: str,
            arg_contract: str = "",
            arg_day: int = 0,
            arg_month: int = 0,
            arg_year: int = 0,
            arg_range: int = 0,
            arg_pg_host: str = "",
            arg_pg_port: int = 5432,
            arg_pg_user: str = "",
            arg_pg_password: str = "",
            arg_pg_db: str = ""
    ) -> None:
        # classic ini file
        config = ConfigParser()
        config.read(configuration_file_name)

        self.__data_collection_settings = DataCollectionSettings(
            type=config["DATA_COLLECTION"]["TYPE"],
            contract=arg_contract if arg_contract else config["DATA_COLLECTION"]["CONTRACT"],
            date=datetime.date(
                year=arg_year if arg_year else int(config["DATA_COLLECTION"]["YEAR"]),
                month=arg_month if arg_month else int(config["DATA_COLLECTION"]["MONTH"]),
                day=arg_day if arg_day else int(config["DATA_COLLECTION"]["DAY"])
            ),
            days_range=arg_range if arg_range else int(config["DATA_COLLECTION"]["DAYS_RANGE"])
        )

        self.__data_collection_retry_settings = DataCollectionRetrySettings(
            interval_sec=int(config["DATA_COLLECTION_SETTINGS"]["RETRY_INTERVAL_SEC"]),
            count=int(config["DATA_COLLECTION_SETTINGS"]["RETRY_INTERVAL_COUNT"]),
            delay_between_days_sec=int(config["DATA_COLLECTION_SETTINGS"]["DELAY_BETWEEN_DAY_REQUESTS_SEC"])
        )

        self.__data_storage_pg_settings = DataStorageSettings(
            enabled=True if arg_pg_host else bool(int(config["DATA_STORAGE_PG"]["ENABLED"])),
            host=arg_pg_host if arg_pg_host else config["DATA_STORAGE_PG"]["HOST"],
            port=arg_pg_port if arg_pg_port else int(config["DATA_STORAGE_PG"]["PORT"]),
            user=arg_pg_user if arg_pg_user else config["DATA_STORAGE_PG"]["USER"],
            password=arg_pg_password if arg_pg_password else config["DATA_STORAGE_PG"]["PASSWORD"],
            db=arg_pg_db if arg_pg_db else config["DATA_STORAGE_PG"]["DB"]
        )

    @property
    def data_collection_settings(self) -> DataCollectionSettings:
        return self.__data_collection_settings

    @property
    def data_collection_retry_settings(self) -> DataCollectionRetrySettings:
        return self.__data_collection_retry_settings

    @property
    def data_storage_pg_settings(self) -> DataStorageSettings:
        return self.__data_storage_pg_settings
