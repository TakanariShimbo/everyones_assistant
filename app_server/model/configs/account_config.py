from typing import Type
from textwrap import dedent

import pandas as pd

from ..base import ColumnConfig, BaseColumnConfigEnum, BaseDatabaseConfig


class AccountColumnConfigs(BaseColumnConfigEnum):
    ACCOUNT_ID = ColumnConfig(name="account_id", dtype=pd.StringDtype(), auto_assigned=False)
    MAIL_ADDRESS = ColumnConfig(name="mail_address", dtype=pd.StringDtype(), auto_assigned=False)
    FAMILY_NAME_EN = ColumnConfig(name="family_name_en", dtype=pd.StringDtype(), auto_assigned=False)
    GIVEN_NAME_EN = ColumnConfig(name="given_name_en", dtype=pd.StringDtype(), auto_assigned=False)
    FAMILY_NAME_JP = ColumnConfig(name="family_name_jp", dtype=pd.StringDtype(), auto_assigned=False)
    GIVEN_NAME_JP = ColumnConfig(name="given_name_jp", dtype=pd.StringDtype(), auto_assigned=False)
    HASHED_PASSWORD = ColumnConfig(name="hashed_password", dtype=pd.StringDtype(), auto_assigned=False)
    REGISTERED_AT = ColumnConfig(name="registered_at", dtype=pd.StringDtype(), auto_assigned=True)
    IS_USER = ColumnConfig(name="is_user", dtype=pd.BooleanDtype(), auto_assigned=True)
    IS_ADMINISTRATOR = ColumnConfig(name="is_administrator", dtype=pd.BooleanDtype(), auto_assigned=True)


class AccountConfig(BaseDatabaseConfig):
    @staticmethod
    def _get_column_configs() -> Type[BaseColumnConfigEnum]:
        return AccountColumnConfigs

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
                registered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
                is_user BOOLEAN DEFAULT TRUE NOT NULL,
                is_administrator BOOLEAN DEFAULT FALSE NOT NULL
            );
            """
        )
