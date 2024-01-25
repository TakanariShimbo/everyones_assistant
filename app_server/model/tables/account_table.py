from typing import List, Type

import pandas as pd
from sqlalchemy import Engine

from ..base import BaseDatabaseTable
from ..configs import AccountConfig, AccountColumnConfigs
from ..beans import AccountEntity


class AccountTable(BaseDatabaseTable[AccountConfig, AccountEntity]):
    @staticmethod
    def _get_config_class() -> Type[AccountConfig]:
        return AccountConfig

    @staticmethod
    def _get_bean_class() -> Type[AccountEntity]:
        return AccountEntity

    @classmethod
    def load_specified_accounts_from_database(cls, database_engine: Engine, account_ids: List[str]) -> "AccountTable":
        filter_conditions = [f"{AccountConfig.get_key_column_name()} IN :ids"]
        statement, _ = cls._get_select_sql(filter_conditions=filter_conditions)
        parameters = {"ids": tuple(account_ids)}
        return cls.load_from_database(database_engine=database_engine, statement=statement, parameters=parameters)

    @property
    def display_df(self) -> pd.DataFrame:
        all_column_names = self._get_column_names(ignore_auto_assigned=False)
        hashed_password_name = AccountColumnConfigs.HASHED_PASSWORD.value.name
        display_column_names = [name for name in all_column_names if name != hashed_password_name]
        return self.df.loc[:, display_column_names]

    @property
    def uneditable_columns(self) -> List[str]:
        all_column_names = self._get_column_names(ignore_auto_assigned=False)
        hashed_password_name = AccountColumnConfigs.HASHED_PASSWORD.value.name
        is_user_name = AccountColumnConfigs.IS_USER.value.name
        is_admin_name = AccountColumnConfigs.IS_ADMINISTRATOR.value.name
        return [name for name in all_column_names if name not in [hashed_password_name, is_user_name, is_admin_name]]

    def get_only_edited_table(self, edited_display_df: pd.DataFrame) -> "AccountTable":
        original_df = self._df.copy()
        edited_df = original_df.copy()
        edited_df.update(edited_display_df)

        diff_index = original_df != edited_df
        mask_rows = diff_index.any(axis=1)
        only_edited_df = edited_df[mask_rows]
        return AccountTable(df=only_edited_df)
