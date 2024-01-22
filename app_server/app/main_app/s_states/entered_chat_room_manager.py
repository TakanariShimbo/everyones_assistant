from ...base import BaseSStateHasDefault
from controller import ChatRoomManager


class EnteredChatRoomManager(BaseSStateHasDefault[ChatRoomManager]):
    @staticmethod
    def get_name() -> str:
        return "ENTERED_CHAT_ROOM_MANAGER"
