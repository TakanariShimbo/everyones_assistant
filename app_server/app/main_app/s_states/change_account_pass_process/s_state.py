from ....base import BaseSState
from .processer import Processer
from .processer_manager import ProcesserManager


class ChangeAccountPassProcess(BaseSState[ProcesserManager]):
    @staticmethod
    def get_name() -> str:
        return "CHANGE_ACCOUNT_PASS_PROCESS"

    @staticmethod
    def get_default() -> ProcesserManager:
        return ProcesserManager([Processer])
