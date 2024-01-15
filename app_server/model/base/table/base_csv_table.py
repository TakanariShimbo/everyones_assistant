from abc import ABC
from typing import Optional, TypeVar, Type

import pandas as pd

from ..config import BaseCsvConfig
from ..bean import BaseCsvEntity
from .base_table import BaseTable


C = TypeVar("C", bound=BaseCsvConfig)
B = TypeVar("B", bound=BaseCsvEntity)
T = TypeVar("T", bound="BaseCsvTable")


class BaseCsvTable(BaseTable[C, B], ABC):
    @classmethod
    def _get_csv_filepath(cls) -> str:
        return cls._get_config_class()._get_csv_filepath()

    @classmethod
    def _validate_unique(cls: Type[T], df: pd.DataFrame) -> None:
        for config in cls._get_column_config_list():
            if config.unique and df[config.name].duplicated().any():
                raise ValueError(f"Column {config.name} has duplicate values")

    @classmethod
    def _validate_non_null(cls: Type[T], df: pd.DataFrame) -> None:
        for config in cls._get_column_config_list():
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

    def save_to_csv(self, filepath: Optional[str] = None) -> None:
        if filepath == None:
            filepath = self._get_csv_filepath()
        self._df.to_csv(filepath, index=False, mode="a")
