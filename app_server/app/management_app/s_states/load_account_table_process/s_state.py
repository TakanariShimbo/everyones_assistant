from ....base import BaseSState
from .processer import Processer
from .processer_manager import ProcesserManager


class LoadAccountTableProcess(BaseSState[ProcesserManager]):
    @staticmethod
    def get_name() -> str:
        return "LOAD_ACCOUNT_TABLE_PROCESS"

    @staticmethod
    def get_default() -> ProcesserManager:
        return ProcesserManager([Processer])