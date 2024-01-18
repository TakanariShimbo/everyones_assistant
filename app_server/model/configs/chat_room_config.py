from typing import Type
from textwrap import dedent

import pandas as pd

from ..base import ColumnConfig, BaseColumnConfigEnum, BaseDatabaseConfig


class ChatRoomColumnConfigs(BaseColumnConfigEnum):
    ROOM_ID = ColumnConfig(name="room_id", dtype=pd.StringDtype(), auto_assigned=False)
    ACCOUNT_ID = ColumnConfig(name="account_id", dtype=pd.StringDtype(), auto_assigned=False)
    TITLE = ColumnConfig(name="title", dtype=pd.StringDtype(), auto_assigned=False)
    RELEASE_ID = ColumnConfig(name="release_id", dtype=pd.StringDtype(), auto_assigned=False)
    CREATED_AT = ColumnConfig(name="created_at", dtype=pd.StringDtype(), auto_assigned=True)
    IS_DISABLED = ColumnConfig(name="is_disabled", dtype=pd.BooleanDtype(), auto_assigned=True)


class ChatRoomConfig(BaseDatabaseConfig):
    @staticmethod
    def _get_column_configs() -> Type[BaseColumnConfigEnum]:
        return ChatRoomColumnConfigs

    @staticmethod
    def _get_database_table_name() -> str:
        return "chat_rooms"
    
    @staticmethod
    def _get_database_table_creation_sql(table_name: str) -> str:
        return dedent(
            f"""
            CREATE TABLE {table_name} (
                room_id VARCHAR(255) PRIMARY KEY,
                account_id VARCHAR(255) NOT NULL,
                title VARCHAR(255) NOT NULL,
                release_id VARCHAR(255) NOT NULL,
                created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                is_disabled BOOLEAN NOT NULL DEFAULT FALSE,
                FOREIGN KEY (account_id) REFERENCES accounts (account_id) ON DELETE CASCADE
            );
            """
        )
