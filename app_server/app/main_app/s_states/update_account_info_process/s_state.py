from .processer import Processer
from .processer_manager import ProcesserManager
from ....base import BaseSStateHasDefault


class UpdateAccountInfoProcess(BaseSStateHasDefault[ProcesserManager]):
    @staticmethod
    def get_name() -> str:
        return "UPDATE_ACCOUNT_INFO_PROCESS"

    @staticmethod
    def get_default() -> ProcesserManager:
        return ProcesserManager([Processer])
