from ....base import BaseSState
from .processer import Processer
from .processer_manager import ProcesserManager


class SignUpProcess(BaseSState[ProcesserManager]):
    @staticmethod
    def get_name() -> str:
        return "SIGN_UP_PROCESS"

    @staticmethod
    def get_default() -> ProcesserManager:
        return ProcesserManager([Processer])
