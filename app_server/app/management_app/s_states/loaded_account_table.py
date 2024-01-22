from ...base import BaseSStateNoDefault
from model import AccountTable


class LoadedAccountTable(BaseSStateNoDefault[AccountTable]):
    @staticmethod
    def get_name() -> str:
        return "LOADED_ACCOUNT_TABLE"
