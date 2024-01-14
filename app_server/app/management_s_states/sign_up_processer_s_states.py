from .sign_up_processers import SignUpProcesser, SignUpProcesserManager
from ..base import BaseSState


class SignUpProcesserSState(BaseSState[SignUpProcesserManager]):
    @staticmethod
    def get_name() -> str:
        return "SIGN_UP_PROCESSER_MANAGER"

    @staticmethod
    def get_default() -> SignUpProcesserManager:
        return SignUpProcesserManager([SignUpProcesser])
