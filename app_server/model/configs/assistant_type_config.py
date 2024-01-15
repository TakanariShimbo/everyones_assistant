from typing import Type

import pandas as pd

from ..static import TablePathes
from ..base import ColumnConfig, BaseColumnConfigEnum, BaseCsvConfig


class AssistantTypeColumnConfigs(BaseColumnConfigEnum):
    ASSISTANT_ID = ColumnConfig(name="assistant_id", dtype=pd.StringDtype(), unique=True, non_null=True, auto_assigned=False)
    PROVIDER_ID = ColumnConfig(name="provider_id", dtype=pd.StringDtype(), unique=False, non_null=True, auto_assigned=False)
    AI_MODEL_ID = ColumnConfig(name="ai_model_id", dtype=pd.StringDtype(), unique=False, non_null=True, auto_assigned=False)
    LABEL_EN = ColumnConfig(name="label_en", dtype=pd.StringDtype(), unique=True, non_null=True, auto_assigned=False)
    LABEL_JP = ColumnConfig(name="label_jp", dtype=pd.StringDtype(), unique=True, non_null=True, auto_assigned=False)


class AssistantTypeConfig(BaseCsvConfig):
    @staticmethod
    def _get_column_configs() -> Type[BaseColumnConfigEnum]:
        return AssistantTypeColumnConfigs

    @staticmethod
    def _get_csv_filepath() -> str:
        return TablePathes.ASSISTNAT
