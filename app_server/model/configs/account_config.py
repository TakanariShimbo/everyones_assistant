from typing import List
from textwrap import dedent

import pandas as pd

from ..base import ColumnConfig, BaseConfig


class AccountConfig(BaseConfig):
    @staticmethod
    def _get_column_configs() -> List[ColumnConfig]:
        return [
            ColumnConfig(name="account_id", dtype=pd.StringDtype(), auto_assigned=False),
            ColumnConfig(name="mail_address", dtype=pd.StringDtype(), auto_assigned=False),
            ColumnConfig(name="family_name_en", dtype=pd.StringDtype(), auto_assigned=False),
            ColumnConfig(name="given_name_en", dtype=pd.StringDtype(), auto_assigned=False),
            ColumnConfig(name="family_name_jp", dtype=pd.StringDtype(), auto_assigned=False),
            ColumnConfig(name="given_name_jp", dtype=pd.StringDtype(), auto_assigned=False),
            ColumnConfig(name="hashed_password", dtype=pd.StringDtype(), auto_assigned=False),
            ColumnConfig(name="registered_at", dtype=pd.StringDtype(), auto_assigned=True),
        ]

    @staticmethod
    def _get_database_table_name() -> str:
        return "accounts"
    
    @staticmethod
    def _get_database_table_creation_sql(table_name: str) -> str:
        return dedent(
            f"""
            CREATE TABLE {table_name} (
                account_id VARCHAR(255) PRIMARY KEY,
                mail_address VARCHAR(255) NOT NULL UNIQUE,
                family_name_en VARCHAR(255) NOT NULL,
                given_name_en VARCHAR(255) NOT NULL,
                family_name_jp VARCHAR(255) NOT NULL,
                given_name_jp VARCHAR(255) NOT NULL,
                hashed_password VARCHAR(255) NOT NULL,
                registered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            """
        )
