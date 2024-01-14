from .sign_in_processers import SignInProcesser, SignInProcesserManager
from ..base import BaseSState


class SignInProcesserSState(BaseSState[SignInProcesserManager]):
    @staticmethod
    def get_name() -> str:
        return "SIGN_IN_PROCESSER_MANAGER"

    @staticmethod
    def get_default() -> SignInProcesserManager:
        return SignInProcesserManager([SignInProcesser])
