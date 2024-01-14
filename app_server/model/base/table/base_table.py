from abc import ABC, abstractmethod
from typing import Any, Dict, List, Generic, TypeVar, Type

import pandas as pd
from pandas.api.extensions import ExtensionDtype

from ..column_config import ColumnConfig
from ..config import BaseConfig
from ..bean import BaseBean


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
