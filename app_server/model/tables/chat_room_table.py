from typing import Type

from sqlalchemy import Engine

from ..base import BaseTable
from ..configs import ChatRoomConfig, AccountConfig, ReleaseTypeConfig
from ..beans import ChatRoomEntity
from .release_type_table import RELEASE_TYPE_TABLE


class ChatRoomTable(BaseTable[ChatRoomConfig, ChatRoomEntity]):
    @staticmethod
    def _get_config_class() -> Type[ChatRoomConfig]:
        return ChatRoomConfig

    @staticmethod
    def _get_bean_class() -> Type[ChatRoomEntity]:
        return ChatRoomEntity

    @classmethod
    def load_specified_account_from_database(cls, database_engine: Engine, account_id: str, limit: int = 5) -> "ChatRoomTable":
        account_id_name = AccountConfig.get_key_column_name()
        filter_conditions = [f"{account_id_name} = :{account_id_name}"]
        order_condition = f"created_at DESC"
        statement, _ = cls._get_select_sql(filter_conditions=filter_conditions, order_condition=order_condition, limit=limit)
        parameters = {account_id_name: account_id}
        return cls.load_from_database(database_engine=database_engine, statement=statement, parameters=parameters)

    @classmethod
    def load_public_unspecified_account_from_database(cls, database_engine: Engine, account_id: str, limit: int = 5) -> "ChatRoomTable":
        account_id_name = AccountConfig.get_key_column_name()
        release_id_name = ReleaseTypeConfig.get_key_column_name()
        filter_conditions = [f"{release_id_name} = :{release_id_name}", f"{account_id_name} != :{account_id_name}"]
        order_condition = "created_at DESC"
        statement, _ = cls._get_select_sql(filter_conditions=filter_conditions, order_condition=order_condition, limit=limit)
        parameters = {release_id_name: RELEASE_TYPE_TABLE.public_id, account_id_name: account_id}
        return cls.load_from_database(database_engine=database_engine, statement=statement, parameters=parameters)

