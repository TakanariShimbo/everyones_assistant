from .query_processers import QueryProcesser, QueryProcesserManager
from ..base import BaseSState


class QueryProcesserSState(BaseSState[QueryProcesserManager]):
    @staticmethod
    def get_name() -> str:
        return "QUERY_PROCESSER_MANAGER"

    @staticmethod
    def get_default() -> QueryProcesserManager:
        return QueryProcesserManager([QueryProcesser])
