from ...base import BaseSStateNoDefault
from controller import ChatRoomManager


class EnteredChatRoomManager(BaseSStateNoDefault[ChatRoomManager]):
    @staticmethod
    def get_name() -> str:
        return "ENTERED_CHAT_ROOM_MANAGER"
