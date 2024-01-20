from .processer import SignInProcesser
from .processer_manager import SignInProcesserManager
from ....base import BaseSState


class SignInProcess(BaseSState[SignInProcesserManager]):
    @staticmethod
    def get_name() -> str:
        return "SIGN_IN_PROCESS"

    @staticmethod
    def get_default() -> SignInProcesserManager:
        return SignInProcesserManager([SignInProcesser])
