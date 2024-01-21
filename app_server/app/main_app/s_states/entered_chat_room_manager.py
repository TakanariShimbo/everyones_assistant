from ...base import BaseSState
from controller import ChatRoomManager


class EnteredChatRoomManager(BaseSState[ChatRoomManager]):
    @staticmethod
    def get_name() -> str:
        return "ENTERED_CHAT_ROOM_MANAGER"
