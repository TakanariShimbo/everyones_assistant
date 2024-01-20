from ....base import BaseSState
from .processer import Processer
from .processer_manager import ProcesserManager


class CreateRoomProcess(BaseSState[ProcesserManager]):
    @staticmethod
    def get_name() -> str:
        return "CREATE_ROOM_PROCESS"

    @staticmethod
    def get_default() -> ProcesserManager:
        return ProcesserManager([Processer])

