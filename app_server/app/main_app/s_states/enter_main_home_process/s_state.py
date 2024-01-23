from ....base import BaseSStateHasDefault
from .processer import Processer
from .processer_manager import ProcesserManager


class EnterMainHomeProcess(BaseSStateHasDefault[ProcesserManager]):
    @staticmethod
    def get_name() -> str:
        return "ENTER_MAIN_HOME_PROCESS"

    @staticmethod
    def get_default() -> ProcesserManager:
        return ProcesserManager([Processer])
