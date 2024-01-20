from .processer import Processer
from .processer_manager import ProcesserManager
from ....base import BaseSState


class QueryProcess(BaseSState[ProcesserManager]):
    @staticmethod
    def get_name() -> str:
        return "QUERY_PROCESS"

    @staticmethod
    def get_default() -> ProcesserManager:
        return ProcesserManager([Processer])
