from ....base import BaseSStateHasDefault
from .processer import Processer
from .processer_manager import ProcesserManager


class DeleteChatRoomProcess(BaseSStateHasDefault[ProcesserManager]):
    @staticmethod
    def get_name() -> str:
        return "DELETE_CHAT_ROOM_PROCESS"

    @staticmethod
    def get_default() -> ProcesserManager:
        return ProcesserManager([Processer])

