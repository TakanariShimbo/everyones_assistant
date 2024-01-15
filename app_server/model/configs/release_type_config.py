from typing import Type

import pandas as pd

from ..static import TablePathes
from ..base import ColumnConfig, BaseColumnConfigEnum, BaseCsvConfig


class ReleaseTypeColumnConfigs(BaseColumnConfigEnum):
    RELEASE_ID = ColumnConfig(name="release_id", dtype=pd.StringDtype(), unique=True, non_null=True, auto_assigned=False)
    LABEL_EN = ColumnConfig(name="label_en", dtype=pd.StringDtype(), unique=True, non_null=True, auto_assigned=False)
    LABEL_JP = ColumnConfig(name="label_jp", dtype=pd.StringDtype(), unique=True, non_null=True, auto_assigned=False)


class ReleaseTypeConfig(BaseCsvConfig):
    @staticmethod
    def _get_column_configs() -> Type[BaseColumnConfigEnum]:
        return ReleaseTypeColumnConfigs

    @staticmethod
    def _get_csv_filepath() -> str:
        return TablePathes.RELEASE
