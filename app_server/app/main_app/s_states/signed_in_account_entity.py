from ...base import BaseSStateNoDefault
from model import AccountEntity


class SignedInAccountEntity(BaseSStateNoDefault[AccountEntity]):
    @staticmethod
    def get_name() -> str:
        return "SIGNED_IN_ACCOUNT_ENTITY"
