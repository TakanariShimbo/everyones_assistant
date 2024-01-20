from .processer import Processer
from .processer_manager import ProcesserManager
from ....base import BaseSState


class EnterRoomProcess(BaseSState[ProcesserManager]):
    @staticmethod
    def get_name() -> str:
        return "ENTER_ROOM_PROCESS"

    @staticmethod
    def get_default() -> ProcesserManager:
        return ProcesserManager([Processer])
