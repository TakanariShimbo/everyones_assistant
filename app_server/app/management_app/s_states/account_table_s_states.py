from ...base import BaseSState
from model import AccountTable


class AccountTableSState(BaseSState[AccountTable]):
    @staticmethod
    def get_name() -> str:
        return "LOADED_ACCOUNT_TABLE"
