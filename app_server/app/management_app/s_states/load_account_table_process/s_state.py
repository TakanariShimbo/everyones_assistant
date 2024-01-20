from .processer import Processer
from .processer_manager import ProcesserManager
from ....base import BaseSState


class LoadAccountTableProcess(BaseSState[ProcesserManager]):
    @staticmethod
    def get_name() -> str:
        return "LOAD_ACCOUNT_TABLE_PROCESS"

    @staticmethod
    def get_default() -> ProcesserManager:
        return ProcesserManager([Processer])