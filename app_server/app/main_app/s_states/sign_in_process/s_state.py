from ....base import BaseSState
from .processer import Processer
from .processer_manager import ProcesserManager


class SignInProcess(BaseSState[ProcesserManager]):
    @staticmethod
    def get_name() -> str:
        return "SIGN_IN_PROCESS"

    @staticmethod
    def get_default() -> ProcesserManager:
        return ProcesserManager([Processer])
