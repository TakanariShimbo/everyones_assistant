from typing import Type

import pandas as pd

from ..static import TablePathes
from ..base import ColumnConfig, BaseColumnConfigEnum, BaseCsvConfig


class MainComponentTypeColumnConfigs(BaseColumnConfigEnum):
    COMPONENT_ID = ColumnConfig(name="component_id", dtype=pd.StringDtype(), unique=True, non_null=True, auto_assigned=False)
    LABEL_EN = ColumnConfig(name="label_en", dtype=pd.StringDtype(), unique=True, non_null=True, auto_assigned=False)
    LABEL_JP = ColumnConfig(name="label_jp", dtype=pd.StringDtype(), unique=True, non_null=True, auto_assigned=False)


class MainComponentTypeConfig(BaseCsvConfig):
    @staticmethod
    def _get_column_configs() -> Type[BaseColumnConfigEnum]:
        return MainComponentTypeColumnConfigs

    @staticmethod
    def _get_csv_filepath() -> str:
        return TablePathes.MAIN_COMPONENT
