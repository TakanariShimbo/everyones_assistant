from .. import s_states as SStates


class ChatRoomPreComponent:
    @staticmethod
    def init() -> None:
        SStates.CurrentComponentEntity.init()
        SStates.EnteredChatRoomManager.init()

    @staticmethod
    def prepare() -> None:
        SStates.CurrentComponentEntity.set_chat_room_entity()

    @staticmethod
    def deinit() -> None:
        pass
