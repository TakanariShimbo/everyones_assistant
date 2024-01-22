from ....base import BaseSStateHasDefault
from .processer import Processer
from .processer_manager import ProcesserManager


class SignUpProcess(BaseSStateHasDefault[ProcesserManager]):
    @staticmethod
    def get_name() -> str:
        return "SIGN_UP_PROCESS"

    @staticmethod
    def get_default() -> ProcesserManager:
        return ProcesserManager([Processer])
