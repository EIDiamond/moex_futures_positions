import logging
import os
import sys
import argparse

from logging.handlers import RotatingFileHandler

from configuration.configuration import ProgramConfiguration
from data_collector.data_collector_factory import DataCollectorFactory

# the configuration file name
CONFIG_FILE = "settings.ini"

logger = logging.getLogger(__name__)


def prepare_logs():
    if not os.path.exists("logs/"):
        os.makedirs("logs/")

    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s",
        handlers=[RotatingFileHandler('logs/collector.log', maxBytes=100000000, backupCount=10, encoding='utf-8')],
        encoding="utf-8"
    )


if __name__ == '__main__':
    prepare_logs()

    logger.info("Program has been started")

    logger.info(f"Program arguments: {sys.argv}")
    parser = argparse.ArgumentParser()
    parser.add_argument("--contract", help="futures contract name", type=str, default="")
    parser.add_argument("--day", help="day of requesting date", type=int, default="0")
    parser.add_argument("--month", help="month of requesting date", type=int, default="0")
    parser.add_argument("--year", help="year of requesting date", type=int, default="0")
    args = parser.parse_args()

    logger.info(f"Parsed arguments: {args}")

    try:
        config = ProgramConfiguration(
            CONFIG_FILE,
            arg_contract=args.contract,
            arg_day=args.day,
            arg_month=args.month,
            arg_year=args.year
        )
        logger.info("Configuration has been loaded")

        logger.info(f"Start collect contract: {config.data_collection_settings.contract};"
                    f" date: {config.data_collection_settings.date};"
                    f" retry settings: {config.data_collection_retry_settings};"
                    f" collector type: {config.data_collection_settings.type}")

        collector = DataCollectorFactory.new_factory(
            config.data_collection_settings.type,
            config.data_collection_retry_settings
        )
        logger.info("Collector has been loaded")

        try:
            result = collector.download(
                config.data_collection_settings.date,
                config.data_collection_settings.contract
            )

            logger.info(f"Collect results: {result}")
            print(f"Collect results:")
            print(f"{result}")
        except Exception as ex:
            logger.error(f"Collect error has been occurred: {repr(ex)}")

    except Exception as ex:
        logger.error(f"Error has been occurred: {repr(ex)}")

    logger.info("Program has been finished.")
