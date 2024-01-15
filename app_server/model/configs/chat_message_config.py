from typing import List
from textwrap import dedent

import pandas as pd

from ..base import ColumnConfig, BaseColumnConfigEnum, BaseDatabaseConfig


class ChatMessageColumnConfigs(BaseColumnConfigEnum):
    MESSAGE_SERIAL_ID = ColumnConfig(name="message_serial_id", dtype=pd.Int64Dtype(), auto_assigned=True)
    ROOM_ID = ColumnConfig(name="room_id", dtype=pd.StringDtype(), auto_assigned=False)
    SENDER_ID = ColumnConfig(name="sender_id", dtype=pd.StringDtype(), auto_assigned=False)
    ROLE_ID = ColumnConfig(name="role_id", dtype=pd.StringDtype(), auto_assigned=False)
    CONTENT = ColumnConfig(name="content", dtype=pd.StringDtype(), auto_assigned=False)
    SENT_AT = ColumnConfig(name="sent_at", dtype=pd.StringDtype(), auto_assigned=True)


class ChatMessageConfig(BaseDatabaseConfig):
    @staticmethod
    def _get_column_configs() -> List[ColumnConfig]:
        return ChatMessageColumnConfigs.to_list()

    @staticmethod
    def _get_database_table_name() -> str:
        return "chat_messages"
    
    @staticmethod
    def _get_database_table_creation_sql(table_name: str) -> str:
        return dedent(
            f"""
            CREATE TABLE {table_name} (
                message_serial_id SERIAL PRIMARY KEY,
                room_id VARCHAR(255) NOT NULL,
                sender_id VARCHAR(255) NOT NULL,
                role_id VARCHAR(255) NOT NULL,
                content TEXT NOT NULL,
                sent_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (room_id) REFERENCES chat_rooms (room_id) ON DELETE CASCADE
            );
            """
        )
