from ....base import BaseSStateHasDefault
from .processer import Processer
from .processer_manager import ProcesserManager


class ChangeAccountPassProcess(BaseSStateHasDefault[ProcesserManager]):
    @staticmethod
    def get_name() -> str:
        return "CHANGE_ACCOUNT_PASS_PROCESS"

    @staticmethod
    def get_default() -> ProcesserManager:
        return ProcesserManager([Processer])
