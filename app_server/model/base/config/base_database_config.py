from abc import ABC, abstractmethod

from sqlalchemy import Engine

from ...handler import DatabaseHandler
from .base_config import BaseConfig


class BaseDatabaseConfig(BaseConfig, ABC):
    @staticmethod
    @abstractmethod
    def _get_database_table_name() -> str:
        raise NotImplementedError("Subclasses must implement this method")

    @staticmethod
    @abstractmethod
    def _get_database_table_creation_sql(table_name: str) -> str:
        raise NotImplementedError("Subclasses must implement this method")

    @classmethod
    def create_table_on_database(cls, database_engine: Engine) -> None:
        DatabaseHandler.execute_sql(
            database_engine=database_engine,
            statement=cls._get_database_table_creation_sql(table_name=cls._get_database_table_name()),
            parameters=None,
        )
