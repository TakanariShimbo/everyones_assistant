from ....base import BaseSStateHasDefault
from .processer import Processer
from .processer_manager import ProcesserManager


class LoadAccountTableProcess(BaseSStateHasDefault[ProcesserManager]):
    @staticmethod
    def get_name() -> str:
        return "LOAD_ACCOUNT_TABLE_PROCESS"

    @staticmethod
    def get_default() -> ProcesserManager:
        return ProcesserManager([Processer])