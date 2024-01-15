from typing import Type

import pandas as pd
from sqlalchemy import Engine

from ..base import BaseDtoTable
from ..configs import ChatRoomDtoConfig, AccountConfig, ReleaseTypeConfig
from ..beans import ChatRoomDto
from .chat_room_table import ChatRoomTable
from .account_table import AccountTable
from .release_type_table import RELEASE_TYPE_TABLE


class ChatRoomDtoTable(BaseDtoTable[ChatRoomDtoConfig, ChatRoomDto]):
    @staticmethod
    def _get_config_class() -> Type[ChatRoomDtoConfig]:
        return ChatRoomDtoConfig

    @staticmethod
    def _get_bean_class() -> Type[ChatRoomDto]:
        return ChatRoomDto

    @classmethod
    def init_from_tables(cls, chat_room_table: ChatRoomTable, account_table: AccountTable) -> "ChatRoomDtoTable":
        chat_room_df = cls._add_prefix_to_columns_except_id(df=chat_room_table.df.copy(), prefix="room_")
        account_df = cls._add_prefix_to_columns_except_id(df=account_table.df.copy(), prefix="account_")
        release_type_df = cls._add_prefix_to_columns_except_id(df=RELEASE_TYPE_TABLE.df.copy(), prefix="release_")
        merged_df = pd.merge(chat_room_df, account_df, on=AccountConfig.get_key_column_name(), how='left')
        merged_df = pd.merge(merged_df, release_type_df, on=ReleaseTypeConfig.get_key_column_name(), how='left')
        return cls(df=merged_df)

    @classmethod
    def load_specified_account_from_database(cls, database_engine: Engine, account_id: str, limit: int = 5) -> "ChatRoomDtoTable":
        chat_room_table = ChatRoomTable.load_specified_account_from_database(
            database_engine=database_engine, 
            account_id=account_id, 
            limit=limit,
        )
        
        account_table = AccountTable.load_specified_accounts_from_database(
            database_engine=database_engine, 
            account_ids=[account_id],
        )
        
        return cls.init_from_tables(chat_room_table=chat_room_table, account_table=account_table)


    @classmethod
    def load_public_unspecified_account_from_database(cls, database_engine: Engine, account_id: str, limit: int = 5) -> "ChatRoomDtoTable":
        chat_room_table = ChatRoomTable.load_public_unspecified_account_from_database(
            database_engine=database_engine, 
            account_id=account_id, 
            limit=limit,
        )
        
        account_ids = chat_room_table.get_unique_values(column_name=AccountConfig.get_key_column_name())
        if len(account_ids) == 0:
            return cls.create_empty_table()
        
        account_table = AccountTable.load_specified_accounts_from_database(
            database_engine=database_engine, 
            account_ids=account_ids,
        )
        return cls.init_from_tables(chat_room_table=chat_room_table, account_table=account_table)