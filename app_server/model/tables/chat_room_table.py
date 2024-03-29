from typing import Type

from sqlalchemy import Engine

from ..base import BaseDatabaseTable
from ..configs import ChatRoomConfig, ChatRoomColumnConfigs, AccountConfig, ReleaseTypeConfig
from ..beans import ChatRoomEntity
from .release_type_table import RELEASE_TYPE_TABLE


class ChatRoomTable(BaseDatabaseTable[ChatRoomConfig, ChatRoomEntity]):
    @staticmethod
    def _get_config_class() -> Type[ChatRoomConfig]:
        return ChatRoomConfig

    @staticmethod
    def _get_bean_class() -> Type[ChatRoomEntity]:
        return ChatRoomEntity

    @classmethod
    def load_not_disabled_and_specified_account_from_database(cls, database_engine: Engine, account_id: str, limit: int = 5) -> "ChatRoomTable":
        account_id_name = AccountConfig.get_key_column_name()
        created_at_name = ChatRoomColumnConfigs.CREATED_AT.value.name
        is_disabled_name = ChatRoomColumnConfigs.IS_DISABLED.value.name
        filter_conditions = [f"{account_id_name} = :{account_id_name}", f"{is_disabled_name} = :{is_disabled_name}"]
        order_condition = f"{created_at_name} DESC"
        statement, _ = cls._get_select_sql(filter_conditions=filter_conditions, order_condition=order_condition, limit=limit)
        parameters = {account_id_name: account_id, is_disabled_name: False}
        return cls.load_from_database(database_engine=database_engine, statement=statement, parameters=parameters)

    @classmethod
    def load_public_and_not_disabled_and_unspecified_account_from_database(cls, database_engine: Engine, account_id: str, limit: int = 5) -> "ChatRoomTable":
        account_id_name = AccountConfig.get_key_column_name()
        release_id_name = ReleaseTypeConfig.get_key_column_name()
        created_at_name = ChatRoomColumnConfigs.CREATED_AT.value.name
        is_disabled_name = ChatRoomColumnConfigs.IS_DISABLED.value.name
        filter_conditions = [f"{release_id_name} = :{release_id_name}", f"{account_id_name} != :{account_id_name}", f"{is_disabled_name} = :{is_disabled_name}"]
        order_condition = f"{created_at_name} DESC"
        statement, _ = cls._get_select_sql(filter_conditions=filter_conditions, order_condition=order_condition, limit=limit)
        parameters = {release_id_name: RELEASE_TYPE_TABLE.PUBLIC_ID, account_id_name: account_id, is_disabled_name: False}
        return cls.load_from_database(database_engine=database_engine, statement=statement, parameters=parameters)
