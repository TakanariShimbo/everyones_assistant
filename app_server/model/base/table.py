from abc import ABC, abstractmethod
from typing import Any, Dict, List, Generic, Literal, Optional, Tuple, TypeVar, Type

import pandas as pd
from pandas.api.extensions import ExtensionDtype
from sqlalchemy import Engine

from ..handler import DatabaseHandler
from .column_config import ColumnConfig
from .config import BaseConfig
from .bean import BaseBean


C = TypeVar("C", bound=BaseConfig)
B = TypeVar("B", bound=BaseBean)
T = TypeVar("T", bound="BaseTable")


class BaseTable(Generic[C, B], ABC):
    @staticmethod
    @abstractmethod
    def _get_config_class() -> Type[C]:
        raise NotImplementedError("Subclasses must implement this method")

    @staticmethod
    @abstractmethod
    def _get_bean_class() -> Type[B]:
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

    @staticmethod
    def _add_prefix_to_columns_except_id(df: pd.DataFrame, prefix: str) -> pd.DataFrame:
        new_columns = {col: prefix + col if not col.endswith('_id') else col for col in df.columns}
        df.rename(columns=new_columns, inplace=True)
        return df

    def __init__(self, df: pd.DataFrame) -> None:
        self._validate_column_names(df=df)
        self._df = df

    def _validate_column_names(self, df: pd.DataFrame):
        if set(df.columns) != set(self._get_column_names(ignore_auto_assigned=False)):
            raise ValueError("DataFrame columns do not match expected columns.")

    @property
    def df(self) -> pd.DataFrame:
        return self._df

    @classmethod
    def append_b_to_a(cls: Type[T], table_a: T, table_b: T) -> T:
        df = pd.concat([table_a.df, table_b.df], ignore_index=True)
        return cls(df)

    @classmethod
    def load_from_beans(cls: Type[T], beans: List[B]) -> T:
        bean_dicts = [bean.to_dict(ignore_auto_assigned=False) for bean in beans]
        df = pd.DataFrame(data=bean_dicts).astype(dtype=cls._get_dtype_dict())
        return cls(df)

    @classmethod
    def _validate_unique(cls: Type[T], df: pd.DataFrame) -> None:
        for config in cls._get_column_configs():
            if config.unique and df[config.name].duplicated().any():
                raise ValueError(f"Column {config.name} has duplicate values")

    @classmethod
    def _validate_non_null(cls: Type[T], df: pd.DataFrame) -> None:
        for config in cls._get_column_configs():
            if config.non_null and df[config.name].isnull().any():
                raise ValueError(f"Column {config.name} has null values")

    @classmethod
    def load_from_csv(cls: Type[T], filepath: Optional[str] = None) -> T:
        if filepath == None:
            filepath = cls._get_csv_filepath()
        df = pd.read_csv(filepath, dtype=cls._get_dtype_dict())
        cls._validate_unique(df=df)
        cls._validate_non_null(df=df)
        return cls(df)

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
    def create_empty_table(cls: Type[T]) -> T:
        series_dict = {name: pd.Series(dtype=dtype) for name, dtype in cls._get_dtype_dict().items()}
        df = pd.DataFrame(series_dict)
        return cls(df)

    def get_all_beans(self) -> List[B]:
        return [self._get_bean_class().init_from_dict(bean_dict=bean_series) for _, bean_series in self._df.iterrows()]

    def get_bean(self, column_name: str, value: Any) -> B:
        rows_mask = self._df.loc[:, column_name] == value
        matching_df = self._df.loc[rows_mask, :]
        if matching_df.empty:
            raise ValueError(f"No rows found for {column_name}={value}")
        elif matching_df.shape[0] > 1:
            raise ValueError(f"Multiple rows found for {column_name}={value}")
        bean_series = matching_df.iloc[0]
        return self._get_bean_class().init_from_dict(bean_dict=bean_series)

    def get_unique_values(self, column_name: str) -> List[Any]:
        return self._df.loc[:, column_name].unique().tolist()

    @classmethod
    def _get_simple_select_sql(cls, column_name: str, value: Any) -> Tuple[str, Dict[str, Any]]:
        table_name = cls._get_database_table_name()
        return DatabaseHandler.get_simple_select_sql(table_name=table_name, column_name=column_name, value=value)

    @classmethod
    def _get_select_sql(cls, filter_conditions: List[str], order_condition: Optional[str] = None, limit: Optional[int] = None) -> Tuple[str, None]:
        table_name = cls._get_database_table_name()
        return DatabaseHandler.get_select_sql(table_name=table_name, filter_conditions=filter_conditions, order_condition=order_condition, limit=limit)

    @classmethod
    def _get_truncate_temp_sql(cls) -> Tuple[str, None]:
        return DatabaseHandler.get_truncate_sql(table_name=cls._get_temp_database_table_name())

    @classmethod
    def _get_upsert_sql(cls) -> Tuple[str, None]:
        """
        NOTES: KEY COLUMN MUST BE 'AUTO_ASSIGNED'=FALSE.
        """
        column_names = cls._get_column_names(ignore_auto_assigned=True)

        return DatabaseHandler.get_upsert_sql(
            table_name=cls._get_database_table_name(),
            temp_table_name=cls._get_temp_database_table_name(),
            key_column_name=column_names[0],
            non_key_column_names=column_names[1::],
        )

    def _insert_to_database(self, database_engine: Engine) -> None:
        column_names = self._get_column_names(ignore_auto_assigned=True)
        self._df.loc[:, column_names].to_sql(name=self._get_database_table_name(), con=database_engine, if_exists="append", index=False)

    def _upsert_to_database(self, database_engine: Engine) -> None:
        statement, parameters = self._get_truncate_temp_sql()
        DatabaseHandler.execute_sql(database_engine=database_engine, statement=statement, parameters=parameters)

        column_names = self._get_column_names(ignore_auto_assigned=True)
        self._df.loc[:, column_names].to_sql(name=self._get_temp_database_table_name(), con=database_engine, if_exists="append", index=False)

        statement, parameters = self._get_upsert_sql()
        DatabaseHandler.execute_sql(database_engine=database_engine, statement=statement, parameters=parameters)

    def save_to_database(self, database_engine: Engine, mode: Literal["insert", "upsert"] = "insert") -> None:
        if mode == "insert":
            self._insert_to_database(database_engine=database_engine)
        elif mode == "upsert":
            self._upsert_to_database(database_engine=database_engine)
        else:
            raise NotImplementedError("Not implemented")

    def save_to_csv(self, filepath: Optional[str] = None) -> None:
        if filepath == None:
            filepath = self._get_csv_filepath()
        self._df.to_csv(filepath, index=False, mode="a")
