from abc import ABC, abstractmethod
from typing import Dict, List

from pandas.api.extensions import ExtensionDtype
from sqlalchemy import Engine

from ..handler import DatabaseHandler
from . import ColumnConfig


class BaseConfig(ABC):
    @staticmethod
    @abstractmethod
    def _get_column_configs() -> List[ColumnConfig]:
        raise NotImplementedError("Subclasses must implement this method")

    @staticmethod
    def _get_database_table_name() -> str:
        raise NotImplementedError("Not implemented")

    @staticmethod
    def _get_database_table_creation_sql(table_name: str) -> str:
        raise NotImplementedError("Not implemented")

    @staticmethod
    def _get_csv_filepath() -> str:
        raise NotImplementedError("Not implemented")

    @classmethod
    def _get_column_names(cls, ignore_auto_assigned: bool) -> List[str]:
        if ignore_auto_assigned:
            return [config.name for config in cls._get_column_configs() if not config.auto_assigned]
        else:
            return [config.name for config in cls._get_column_configs()]

    @classmethod
    def _get_dtype_dict(cls) -> Dict[str, ExtensionDtype]:
        return {config.name: config.dtype for config in cls._get_column_configs()}

    @classmethod
    def _get_temp_database_table_name(cls) -> str:
        return f"{cls._get_database_table_name()}_temp"

    @classmethod
    def get_key_column_name(cls) -> str:
        return cls._get_column_names(ignore_auto_assigned=False)[0]

    @classmethod
    def create_table_on_database(cls, database_engine: Engine) -> None:
        DatabaseHandler.execute_sqls(
            database_engine=database_engine,
            statement_and_parameters_list=[
                (cls._get_database_table_creation_sql(table_name=cls._get_database_table_name()), None),
                (cls._get_database_table_creation_sql(table_name=cls._get_temp_database_table_name()), None),
            ],
        )
