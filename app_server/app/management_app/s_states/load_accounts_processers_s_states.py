from .load_accounts_processers import LoadAccountsProcesser, LoadAccountsProcesserManager
from ...base import BaseSState


class LoadAccountsProcesserSState(BaseSState[LoadAccountsProcesserManager]):
    @staticmethod
    def get_name() -> str:
        return "LOAD_ACCOUNTS_PROCESSER_MANAGER"

    @staticmethod
    def get_default() -> LoadAccountsProcesserManager:
        return LoadAccountsProcesserManager([LoadAccountsProcesser])