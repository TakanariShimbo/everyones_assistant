from abc import ABC
from typing import Any, Dict, Tuple, TypeVar, Type

from sqlalchemy import Engine

from ...handler import DatabaseHandler
from ..config import BaseDatabaseConfig
from .base_bean import BaseBean


C = TypeVar("C", bound=BaseDatabaseConfig)
B = TypeVar("B", bound="BaseDatabaseEntity")


class BaseDatabaseEntity(BaseBean[C], ABC):
    @classmethod
    def _get_database_table_name(cls) -> str:
        return cls._get_config_class()._get_database_table_name()

    @classmethod
    def _get_simple_select_sql(cls, column_name: str, value: Any) -> Tuple[str, Dict[str, Any]]:
        table_name = cls._get_database_table_name()
        return DatabaseHandler.get_simple_select_sql(table_name=table_name, column_name=column_name, value=value)

    @classmethod
    def load_from_database(cls: Type[B], database_engine: Engine, column_name: str, value: Any) -> B:
        statement, parameters = cls._get_simple_select_sql(column_name=column_name, value=value)
        results = DatabaseHandler.execute_sql(database_engine=database_engine, statement=statement, parameters=parameters)

        first_result = results.fetchone()
        second_result = results.fetchone()
        if first_result == None:
            raise ValueError(f"No rows found for {column_name}={value}")
        elif second_result != None:
            raise ValueError(f"Multiple rows found for {column_name}={value}")
        return cls.init_from_dict(bean_dict=first_result._asdict())

    def _get_insert_sql(self) -> Tuple[str, Dict[str, Any]]:
        table_name=self._get_database_table_name()
        column_names = self._get_column_names(ignore_auto_assigned=True)

        statement, _ = DatabaseHandler.get_insert_sql(
            table_name=table_name,
            column_names=column_names,
        )
        parameters = self.to_dict(ignore_auto_assigned=True)
        return statement, parameters

    def _get_update_sql(self) -> Tuple[str, Dict[str, Any]]:
        table_name=self._get_database_table_name()
        key_column_name = self._get_key_column_name()
        column_names = self._get_column_names(ignore_auto_assigned=False)
        
        statement, _ = DatabaseHandler.get_update_sql(
            table_name=table_name,
            key_column_name=key_column_name,
            non_key_column_names=[column_name for column_name in column_names if column_name != key_column_name],
        )
        parameters = self.to_dict(ignore_auto_assigned=False)
        return statement, parameters

    def _get_delete_sql(self) -> Tuple[str, Dict[str, Any]]:
        table_name = self._get_database_table_name()
        key_column_name = self._get_key_column_name()
        key_value = getattr(self, key_column_name)

        statement, parameters = DatabaseHandler.get_delete_sql(
            table_name=table_name,
            key_column_name=key_column_name,
            key_value=key_value,
        )
        return statement, parameters

    def insert_record_to_database(self, database_engine: Engine) -> None:
        statement, parameters = self._get_insert_sql()
        DatabaseHandler.execute_sql(database_engine=database_engine, statement=statement, parameters=parameters)

    def update_record_of_database(self, database_engine: Engine) -> None:
        statement, parameters = self._get_update_sql()
        DatabaseHandler.execute_sql(database_engine=database_engine, statement=statement, parameters=parameters)

    def remove_from_database(self, database_engine: Engine) -> None:
        statement, parameters = self._get_delete_sql()
        DatabaseHandler.execute_sql(database_engine=database_engine, statement=statement, parameters=parameters)
