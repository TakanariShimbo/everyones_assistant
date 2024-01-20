from .processer import UpdateAccountInfoProcesser
from .processer_manager import UpdateAccountInfoProcesserManager
from ....base import BaseSState


class UpdateAccountInfoProcess(BaseSState[UpdateAccountInfoProcesserManager]):
    @staticmethod
    def get_name() -> str:
        return "UPDATE_ACCOUNT_INFO_PROCESS"

    @staticmethod
    def get_default() -> UpdateAccountInfoProcesserManager:
        return UpdateAccountInfoProcesserManager([UpdateAccountInfoProcesser])
