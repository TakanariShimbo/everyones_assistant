from .. import s_states as SStates
from model import AccountEntity


class HomePreComponent:
    @staticmethod
    def init() -> None:
        SStates.CurrentComponentEntity.init()

    @staticmethod
    def prepare() -> None:
        SStates.CurrentComponentEntity.set_home_entity()

    @classmethod
    def prepare_for_sign_in(cls, signed_in_account_entity: AccountEntity) -> None:
        SStates.SignedInAccountEntity.set(value=signed_in_account_entity)
        cls.prepare()

    @staticmethod
    def deinit() -> None:
        pass
