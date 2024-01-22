from ....base import BaseSStateHasDefault
from .processer import Processer
from .processer_manager import ProcesserManager


class CreateChatRoomProcess(BaseSStateHasDefault[ProcesserManager]):
    @staticmethod
    def get_name() -> str:
        return "CREATE_CHAT_ROOM_PROCESS"

    @staticmethod
    def get_default() -> ProcesserManager:
        return ProcesserManager([Processer])

