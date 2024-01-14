from typing import List
from uuid import uuid4

from model import ChatRoomEntity, ChatMessageEntity, ChatMessageTable, ROLE_TYPE_TABLE, Database


class ChatRoomManager:
    def __init__(self, chat_message_table: ChatMessageTable, room_id: str, account_id: str, release_id: str):
        self._table = chat_message_table
        self._room_id = room_id
        self._release_id = release_id
        self._account_id = account_id

    @property
    def account_id(self) -> str:
        return self._account_id

    @property
    def release_id(self) -> str:
        return self._release_id

    @classmethod
    def init_as_new(cls, title: str, account_id: str, release_id: str) -> "ChatRoomManager":
        room_id = str(uuid4())
        new_chat_room_entity = ChatRoomEntity(room_id=room_id, account_id=account_id, title=title, release_id=release_id)
        new_chat_room_entity.save_to_database(database_engine=Database.engine)

        chat_message_table = ChatMessageTable.create_empty_table()
        return cls(chat_message_table=chat_message_table, room_id=room_id, account_id=account_id, release_id=release_id)

    @classmethod
    def init_as_continue(cls, room_id: str, account_id: str, release_id: str) -> "ChatRoomManager":
        chat_message_table = ChatMessageTable.load_specified_room_from_database(database_engine=Database.engine, room_id=room_id)
        return cls(chat_message_table=chat_message_table, room_id=room_id, account_id=account_id, release_id=release_id)

    def add_prompt_and_answer(self, prompt: str, answer: str, account_id: str, assistant_id: str) -> None:
        prompt_and_answer_entitys = [
            ChatMessageEntity(room_id=self._room_id, role_id=ROLE_TYPE_TABLE.user_id, sender_id=account_id, content=prompt),
            ChatMessageEntity(room_id=self._room_id, role_id=ROLE_TYPE_TABLE.assistant_id, sender_id=assistant_id, content=answer),
        ]
        appended_table = ChatMessageTable.load_from_beans(beans=prompt_and_answer_entitys)
        appended_table.save_to_database(database_engine=Database.engine)
        self._table = ChatMessageTable.append_b_to_a(self._table, appended_table)

    def get_all_message_entities(self) -> List[ChatMessageEntity]:
        return self._table.get_all_beans()
