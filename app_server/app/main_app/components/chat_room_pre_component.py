from .. import s_states as SStates
from controller import ChatRoomManager


class ChatRoomPreComponent:
    @staticmethod
    def init() -> None:
        SStates.CurrentComponentEntity.init()

    @staticmethod
    def prepare(chat_room_manager: ChatRoomManager) -> None:
        SStates.EnteredChatRoomManager.set(value=chat_room_manager)
        SStates.CurrentComponentEntity.set_chat_room_entity()

    @staticmethod
    def deinit() -> None:
        pass
