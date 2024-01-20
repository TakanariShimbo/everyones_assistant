from ...base import BaseSState
from model import AccountEntity


class SignedInAccountEntitySState(BaseSState[AccountEntity]):
    @staticmethod
    def get_name() -> str:
        return "SIGNED_IN_ACCOUNT_ENTITY"
