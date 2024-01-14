from abc import ABC, abstractmethod
from typing import Any, Dict, List, Literal, Generic, Tuple, TypeVar, Type, Union

import pandas as pd
from pandas.api.extensions import ExtensionDtype
from sqlalchemy import Engine

from ..handler import DatabaseHandler
from .column_config import ColumnConfig
from .config import BaseConfig


C = TypeVar("C", bound=BaseConfig)
B = TypeVar("B", bound="BaseBean")


class BaseBean(Generic[C], ABC):
    @staticmethod
    @abstractmethod
    def _get_config_class() -> Type[C]:
        raise NotImplementedError("Subclasses must implement this method")

    @abstractmethod
    def _check_is_same(self, other: Any) -> bool:
        raise NotImplementedError("Subclasses must implement this method")

    @classmethod
    def _get_column_configs(cls) -> List[ColumnConfig]:
        return cls._get_config_class()._get_column_configs()

    @classmethod
    def _get_csv_filepath(cls) -> str:
        return cls._get_config_class()._get_csv_filepath()

    @classmethod
    def _get_database_table_name(cls) -> str:
        return cls._get_config_class()._get_database_table_name()

    @classmethod
    def _get_temp_database_table_name(cls) -> str:
        return cls._get_config_class()._get_temp_database_table_name()

    @classmethod
    def _get_column_names(cls, ignore_auto_assigned: bool) -> List[str]:
        return cls._get_config_class()._get_column_names(ignore_auto_assigned=ignore_auto_assigned)

    @classmethod
    def _get_dtype_dict(cls) -> Dict[str, ExtensionDtype]:
        return cls._get_config_class()._get_dtype_dict()

    def __eq__(self, other):
        return self._check_is_same(other=other)

    @classmethod
    def init_from_dict(cls: Type[B], bean_dict: Union[Dict[str, Any], pd.Series]) -> B:
        kwargs = {name: None if pd.isna(bean_dict[name]) else bean_dict[name] for name in cls._get_column_names(ignore_auto_assigned=False)}
        return cls(**kwargs)

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

    def to_dict(self, ignore_auto_assigned: bool) -> Dict[str, Any]:
        bean_dict = {}
        for name in self._get_column_names(ignore_auto_assigned=ignore_auto_assigned):
            try:
                bean_dict[name] = getattr(self, name)
            except ValueError:
                bean_dict[name] = None
        return bean_dict

    def _get_insert_sql(self) -> Tuple[str, Dict[str, Any]]:
        statement, _ = DatabaseHandler.get_insert_sql(
            table_name=self._get_database_table_name(),
            column_names=self._get_column_names(ignore_auto_assigned=True),
        )
        parameters = self.to_dict(ignore_auto_assigned=True)
        return statement, parameters

    def _get_update_sql(self) -> Tuple[str, Dict[str, Any]]:
        column_names = self._get_column_names(ignore_auto_assigned=False)
        statement, _ = DatabaseHandler.get_update_sql(
            table_name=self._get_database_table_name(),
            key_column_name=column_names[0],
            non_key_column_names=column_names[1::],
        )
        parameters = self.to_dict(ignore_auto_assigned=False)
        return statement, parameters

    def _get_delete_sql(self) -> Tuple[str, Dict[str, Any]]:
        key_column_name = self._get_column_names(ignore_auto_assigned=False)[0]
        key_value = getattr(self, key_column_name)

        statement, parameters = DatabaseHandler.get_delete_sql(
            table_name=self._get_database_table_name(),
            key_column_name=key_column_name,
            key_value=key_value,
        )
        return statement, parameters

    def save_to_database(self, database_engine: Engine, mode: Literal["insert", "update"] = "insert") -> None:
        if mode == "insert":
            statement, parameters = self._get_insert_sql()
        elif mode == "update":
            statement, parameters = self._get_update_sql()
        else:
            raise NotImplementedError("Not implemented")

        DatabaseHandler.execute_sql(database_engine=database_engine, statement=statement, parameters=parameters)

    def remove_from_database(self, database_engine: Engine) -> None:
        statement, parameters = self._get_delete_sql()
        DatabaseHandler.execute_sql(database_engine=database_engine, statement=statement, parameters=parameters)
