from ...base import BaseSState
from controller import ChatRoomManager


class EnteredRoomManager(BaseSState[ChatRoomManager]):
    @staticmethod
    def get_name() -> str:
        return "ENTERED_ROOM_MANAGER"
