from enum import Enum
from typing import List

import pandas as pd

from ..static import TablePathes
from ..base import ColumnConfig, BaseCsvConfig


class MainComponentTypeColumnConfigs(Enum):
    COMPONENT_ID = ColumnConfig(name="component_id", dtype=pd.StringDtype(), unique=True, non_null=True, auto_assigned=False)
    LABEL_EN = ColumnConfig(name="label_en", dtype=pd.StringDtype(), unique=True, non_null=True, auto_assigned=False)
    LABEL_JP = ColumnConfig(name="label_jp", dtype=pd.StringDtype(), unique=True, non_null=True, auto_assigned=False)

    @classmethod
    def to_list(cls) -> List[ColumnConfig]:
        return [config.value for config in cls]


class MainComponentTypeConfig(BaseCsvConfig):
    @staticmethod
    def _get_column_configs() -> List[ColumnConfig]:
        return MainComponentTypeColumnConfigs.to_list()

    @staticmethod
    def _get_csv_filepath() -> str:
        return TablePathes.MAIN_COMPONENT
