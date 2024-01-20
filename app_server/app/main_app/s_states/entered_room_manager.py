from ...base import BaseSState
from controller import ChatRoomManager


class EnteredRoomManagerSState(BaseSState[ChatRoomManager]):
    @staticmethod
    def get_name() -> str:
        return "ENTERED_ROOM_MANAGER"
