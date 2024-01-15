from enum import Enum
from typing import List
from textwrap import dedent

import pandas as pd

from ..base import ColumnConfig, BaseDatabaseConfig


class ChatRoomColumnConfigs(Enum):
    ROOM_ID = ColumnConfig(name="room_id", dtype=pd.StringDtype(), auto_assigned=False)
    ACCOUNT_ID = ColumnConfig(name="account_id", dtype=pd.StringDtype(), auto_assigned=False)
    TITLE = ColumnConfig(name="title", dtype=pd.StringDtype(), auto_assigned=False)
    RELEASE_ID = ColumnConfig(name="release_id", dtype=pd.StringDtype(), auto_assigned=False)
    CREATED_AT = ColumnConfig(name="created_at", dtype=pd.StringDtype(), auto_assigned=True)

    @classmethod
    def to_list(cls) -> List[ColumnConfig]:
        return [config.value for config in cls]


class ChatRoomConfig(BaseDatabaseConfig):
    @staticmethod
    def _get_column_configs() -> List[ColumnConfig]:
        return ChatRoomColumnConfigs.to_list()

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
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (account_id) REFERENCES accounts (account_id) ON DELETE CASCADE
            );
            """
        )
