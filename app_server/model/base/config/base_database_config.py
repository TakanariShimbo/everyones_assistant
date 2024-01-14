from abc import ABC, abstractmethod

from sqlalchemy import Engine

from ...handler import DatabaseHandler
from .base_config import BaseConfig


class BaseDatabaseConfig(BaseConfig, ABC):
    @staticmethod
    @abstractmethod
    def _get_database_table_name() -> str:
        raise NotImplementedError("Subclasses must implement this method")

    @classmethod
    def _get_temp_database_table_name(cls) -> str:
        return f"{cls._get_database_table_name()}_temp"

    @staticmethod
    @abstractmethod
    def _get_database_table_creation_sql(table_name: str) -> str:
        raise NotImplementedError("Subclasses must implement this method")

    @classmethod
    def create_table_on_database(cls, database_engine: Engine) -> None:
        DatabaseHandler.execute_sqls(
            database_engine=database_engine,
            statement_and_parameters_list=[
                (cls._get_database_table_creation_sql(table_name=cls._get_database_table_name()), None),
                (cls._get_database_table_creation_sql(table_name=cls._get_temp_database_table_name()), None),
            ],
        )
