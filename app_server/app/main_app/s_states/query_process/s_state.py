from .processer import QueryProcesser
from .processer_manager import QueryProcesserManager
from ....base import BaseSState


class QueryProcess(BaseSState[QueryProcesserManager]):
    @staticmethod
    def get_name() -> str:
        return "QUERY_PROCESS"

    @staticmethod
    def get_default() -> QueryProcesserManager:
        return QueryProcesserManager([QueryProcesser])
