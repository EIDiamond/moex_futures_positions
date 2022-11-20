from configparser import ConfigParser

from configuration.settings import DataCollectionRetrySettings, StorageSettings

__all__ = ("ProgramConfiguration")


class ProgramConfiguration:
    """
    Represent configuration
    """
    def __init__(self, file_name: str) -> None:
        # classic ini file
        config = ConfigParser()
        config.read(file_name)

        self.__data_collection_retry_settings = DataCollectionRetrySettings(
            internal_sec=int(config["DATA_COLLECTION_RETRY"]["RETRY_INTERVAL_SEC"]),
            count=int(config["DATA_COLLECTION_RETRY"]["RETRY_INTERVAL_COUNT"])
        )

        self.__storage_settings = StorageSettings(
            root_path=config["STORAGE"]["ROOT_PATH"]
        )

    @property
    def data_collection_retry_settings(self) -> DataCollectionRetrySettings:
        return self.__data_collection_retry_settings

    @property
    def storage_settings(self) -> StorageSettings:
        return self.__storage_settings
