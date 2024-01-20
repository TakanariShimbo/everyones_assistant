from .processer import CreateRoomProcesser
from .processer_manager import CreateRoomProcesserManager
from ....base import BaseSState


class CreateRoomProcessSState(BaseSState[CreateRoomProcesserManager]):
    @staticmethod
    def get_name() -> str:
        return "CREATE_ROOM_PROCESS"

    @staticmethod
    def get_default() -> CreateRoomProcesserManager:
        return CreateRoomProcesserManager([CreateRoomProcesser])

