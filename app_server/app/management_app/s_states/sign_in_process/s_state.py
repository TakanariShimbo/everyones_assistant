from .processer import Processer
from .processer_manager import ProcesserManager
from ....base import BaseSState


class SignInProcess(BaseSState[ProcesserManager]):
    @staticmethod
    def get_name() -> str:
        return "SIGN_IN_PROCESS"

    @staticmethod
    def get_default() -> ProcesserManager:
        return ProcesserManager([Processer])
