from .processer import LoadAccountTableProcesser
from .processer_manager import LoadAccountTableProcesserManager
from ....base import BaseSState


class LoadAccountTableProcess(BaseSState[LoadAccountTableProcesserManager]):
    @staticmethod
    def get_name() -> str:
        return "LOAD_ACCOUNT_TABLE_PROCESS"

    @staticmethod
    def get_default() -> LoadAccountTableProcesserManager:
        return LoadAccountTableProcesserManager([LoadAccountTableProcesser])