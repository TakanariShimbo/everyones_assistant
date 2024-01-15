from typing import List, Type

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
        filter_conditions = [f"{AccountColumnConfigs.get_key_column_name()} IN :ids"]
        statement, _ = cls._get_select_sql(filter_conditions=filter_conditions)
        parameters = {"ids": tuple(account_ids)}
        return cls.load_from_database(database_engine=database_engine, statement=statement, parameters=parameters)
