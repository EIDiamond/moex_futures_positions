import logging

import psycopg2

from configuration.settings import DataStorageSettings
from position.position import OpenPositions

__all__ = ("DataSaverPG")

logger = logging.getLogger(__name__)


class DataSaverPG:
    def __init__(self, settings: DataStorageSettings) -> None:
        self.__settings = settings

    def save_open_positions(self, positions: OpenPositions) -> None:
        if not self.__settings.enabled:
            logger.info(f"DB saver disabled. Positions skipped.")
            return None

        if not (positions.positions and positions.clients):
            logger.info(f"Open positions and(or) clients are empty. Positions skipped.")
            return None

        try:
            logger.info(f"Start saving data to tables")

            connection = psycopg2.connect(
                user=self.__settings.user,
                password=self.__settings.password,
                host=self.__settings.host,
                port=self.__settings.port,
                database=self.__settings.db
            )
            cursor = connection.cursor()

            cursor.execute(""" SELECT day, contract FROM open_positions WHERE day=%s and contract=%s""",
                           (positions.date, positions.contract))
            if cursor.fetchone():
                logger.debug(f"open_positions table already has the record")
            else:
                cursor.execute(""" INSERT INTO open_positions 
                    (contract, day, juridical_long, juridical_short, physical_long, physical_short) 
                    VALUES (%s, %s, %s, %s, %s, %s) """,
                               (positions.contract, positions.date, positions.positions.juridical_long, positions.positions.juridical_short,
                                positions.positions.physical_long, positions.positions.physical_short))
                connection.commit()
                logger.debug(f"open_positions table was updated")

            cursor.execute(""" SELECT day, contract FROM clients_positions WHERE day=%s and contract=%s""",
                           (positions.date, positions.contract))
            if cursor.fetchone():
                logger.debug(f"clients_positions table already has the record")
            else:
                cursor.execute(""" INSERT INTO clients_positions 
                    (contract, day, juridical_long, juridical_short, physical_long, physical_short) 
                    VALUES (%s, %s, %s, %s, %s, %s) """,
                               (positions.contract, positions.date, positions.clients.juridical_long, positions.clients.juridical_short,
                                positions.clients.physical_long, positions.clients.physical_short))
                connection.commit()
                logger.debug(f"clients_positions table was updated")

        except (Exception, psycopg2.Error) as error:
            logger.error(f"DB saver error has been occurred: {repr(error)}")
        finally:
            # closing database connection.
            if connection:
                cursor.close()
                connection.close()
                logger.debug(f"PostgreSQL connection is closed")
