from .processer import EnterRoomProcesser
from .processer_manager import EnterRoomProcesserManager
from ....base import BaseSState


class EnterRoomProcessSState(BaseSState[EnterRoomProcesserManager]):
    @staticmethod
    def get_name() -> str:
        return "ENTER_ROOM_PROCESS"

    @staticmethod
    def get_default() -> EnterRoomProcesserManager:
        return EnterRoomProcesserManager([EnterRoomProcesser])

