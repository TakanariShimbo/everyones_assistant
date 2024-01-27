from abc import ABC
from typing import Any, Dict, List, Optional, Tuple, TypeVar, Type

from sqlalchemy import Engine

from ...handler import DatabaseHandler
from ..config import BaseDatabaseConfig
from ..bean import BaseDatabaseEntity
from .base_table import BaseTable


C = TypeVar("C", bound=BaseDatabaseConfig)
B = TypeVar("B", bound=BaseDatabaseEntity)
T = TypeVar("T", bound="BaseDatabaseTable")


class BaseDatabaseTable(BaseTable[C, B], ABC):
    @classmethod
    def _get_database_table_name(cls) -> str:
        return cls._get_config_class()._get_database_table_name()

    @classmethod
    def load_from_database(cls: Type[T], database_engine: Engine, statement: Optional[str] = None, parameters: Optional[Dict[str, Any]] = None) -> T:
        if statement == None:
            table_name = cls._get_database_table_name()
            statement = f"SELECT * FROM {table_name}"

        df = DatabaseHandler.query_sql_on_pandas(
            database_engine=database_engine,
            statement=statement,
            parameters=parameters,
            dtype_dict=cls._get_dtype_dict(),
        )
        return cls(df)

    @classmethod
    def _get_simple_select_sql(cls, column_name: str, value: Any) -> Tuple[str, Dict[str, Any]]:
        table_name = cls._get_database_table_name()
        return DatabaseHandler.get_simple_select_sql(table_name=table_name, column_name=column_name, value=value)

    @classmethod
    def _get_select_sql(cls, filter_conditions: List[str], order_condition: Optional[str] = None, limit: Optional[int] = None) -> Tuple[str, None]:
        table_name = cls._get_database_table_name()
        return DatabaseHandler.get_select_sql(table_name=table_name, filter_conditions=filter_conditions, order_condition=order_condition, limit=limit)

    @classmethod
    def _get_upsert_sql(cls, record_dicts: List[Dict[str, Any]], ignore_auto_assigned: bool) -> Tuple[str, Dict[str, Any]]:
        """
        NOTES: KEY COLUMN MUST BE 'AUTO_ASSIGNED'=FALSE.
        """
        table_name = cls._get_database_table_name()
        key_column_name = cls._get_key_column_name()
        column_names = cls._get_column_names(ignore_auto_assigned=ignore_auto_assigned)

        return DatabaseHandler.get_upsert_sql(
            table_name=table_name,
            key_column_name=key_column_name,
            non_key_column_names=[column_name for column_name in column_names if column_name != key_column_name],
            record_dicts=record_dicts,
        )

    def insert_records_to_database(self, database_engine: Engine) -> None:
        if self._df.empty:
            return

        column_names = self._get_column_names(ignore_auto_assigned=True)
        self._df.loc[:, column_names].to_sql(name=self._get_database_table_name(), con=database_engine, if_exists="append", index=False)

    def upsert_records_to_database(self, database_engine: Engine) -> None:
        if self._df.empty:
            return

        column_names = self._get_column_names(ignore_auto_assigned=False)
        record_dicts = self._df.loc[:, column_names].to_dict(orient='records')

        statement, parameters = self._get_upsert_sql(record_dicts=record_dicts, ignore_auto_assigned=False)   # type: ignore
        DatabaseHandler.execute_sql(database_engine=database_engine, statement=statement, parameters=parameters)
