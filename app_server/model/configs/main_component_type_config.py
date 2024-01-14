from typing import List

import pandas as pd

from ..base import ColumnConfig, BaseConfig


class MainComponentTypeConfig(BaseConfig):
    @staticmethod
    def _get_column_configs() -> List[ColumnConfig]:
        return [
            ColumnConfig(name="component_id", dtype=pd.StringDtype(), unique=True, non_null=True, auto_assigned=False),
            ColumnConfig(name="label_en", dtype=pd.StringDtype(), unique=True, non_null=True, auto_assigned=False),
            ColumnConfig(name="label_jp", dtype=pd.StringDtype(), unique=True, non_null=True, auto_assigned=False),
        ]

    @staticmethod
    def _get_csv_filepath() -> str:
        return "./model/data/main_component_data.csv"
