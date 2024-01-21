from ....base import BaseSState
from .processer import Processer
from .processer_manager import ProcesserManager


class LoadChatRoomDtoTablesProcess(BaseSState[ProcesserManager]):
    @staticmethod
    def get_name() -> str:
        return "LOAD_CHAT_ROOM_DTO_TABLES_PROCESS"

    @staticmethod
    def get_default() -> ProcesserManager:
        return ProcesserManager([Processer])