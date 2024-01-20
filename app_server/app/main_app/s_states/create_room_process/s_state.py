from .processer import CreateRoomProcesser
from .processer_manager import CreateRoomProcesserManager
from ....base import BaseSState


class CreateRoomProcess(BaseSState[CreateRoomProcesserManager]):
    @staticmethod
    def get_name() -> str:
        return "CREATE_ROOM_PROCESS"

    @staticmethod
    def get_default() -> CreateRoomProcesserManager:
        return CreateRoomProcesserManager([CreateRoomProcesser])

