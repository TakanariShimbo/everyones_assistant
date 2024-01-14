from ..base import BaseSState
from controller import ChatRoomManager


class ChatRoomSState(BaseSState[ChatRoomManager]):
    @staticmethod
    def get_name() -> str:
        return "CHAT_ROOM_MANAGER"
