from typing import List
from uuid import uuid4

from model import ChatRoomEntity, ChatMessageEntity, ChatMessageTable, ROLE_TYPE_TABLE, Database


class ChatRoomManager:
    def __init__(self, chat_room_entity: ChatRoomEntity, chat_message_table: ChatMessageTable):
        self._chat_room_entity = chat_room_entity
        self._chat_message_table = chat_message_table

    @property
    def room_id(self) -> str:
        return self._chat_room_entity.room_id

    @property
    def account_id(self) -> str:
        return self._chat_room_entity.account_id

    @property
    def release_id(self) -> str:
        return self._chat_room_entity.release_id

    @classmethod
    def init_as_new(cls, title: str, account_id: str, release_id: str) -> "ChatRoomManager":
        room_id = str(uuid4())
        new_chat_room_entity = ChatRoomEntity(room_id=room_id, account_id=account_id, title=title, release_id=release_id)
        new_chat_room_entity = new_chat_room_entity.insert_record_to_database(database_engine=Database.ENGINE)

        empty_chat_message_table = ChatMessageTable.create_empty_table()
        return cls(chat_room_entity=new_chat_room_entity, chat_message_table=empty_chat_message_table)

    @classmethod
    def init_as_continue(cls, room_id: str) -> "ChatRoomManager":
        loaded_chat_room_entity = ChatRoomEntity.load_specified_id_from_database(database_engine=Database.ENGINE, room_id=room_id)
        loaded_chat_message_table = ChatMessageTable.load_specified_room_from_database(database_engine=Database.ENGINE, room_id=room_id)
        return cls(chat_room_entity=loaded_chat_room_entity, chat_message_table=loaded_chat_message_table)

    def add_prompt_and_answer(self, prompt: str, answer: str, account_id: str, assistant_id: str) -> None:
        prompt_and_answer_entitys = [
            ChatMessageEntity(room_id=self.room_id, role_id=ROLE_TYPE_TABLE.USER_ID, sender_id=account_id, content=prompt),
            ChatMessageEntity(room_id=self.room_id, role_id=ROLE_TYPE_TABLE.ASSISTANT_ID, sender_id=assistant_id, content=answer),
        ]
        appended_table = ChatMessageTable.load_from_beans(beans=prompt_and_answer_entitys)
        appended_table.insert_records_to_database(database_engine=Database.ENGINE)
        self._chat_message_table = ChatMessageTable.append_b_to_a(self._chat_message_table, appended_table)

    def get_all_message_entities(self) -> List[ChatMessageEntity]:
        return self._chat_message_table.get_all_beans()

    def delete_chat_room(self) -> None:
        self._chat_room_entity.is_disabled = True
        self._chat_room_entity.update_record_of_database(database_engine=Database.ENGINE)
