from .processer import SignUpProcesser
from .processer_manager import SignUpProcesserManager
from ....base import BaseSState


class SignUpProcess(BaseSState[SignUpProcesserManager]):
    @staticmethod
    def get_name() -> str:
        return "SIGN_UP_PROCESS"

    @staticmethod
    def get_default() -> SignUpProcesserManager:
        return SignUpProcesserManager([SignUpProcesser])
