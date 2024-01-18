from .update_account_info_processers import UpdateAccountInfoProcesser, UpdateAccountInfoProcesserManager
from ..base import BaseSState


class UpdateAccountInfoProcesserSState(BaseSState[UpdateAccountInfoProcesserManager]):
    @staticmethod
    def get_name() -> str:
        return "EDIT_ACCOUNT_INFO_PROCESSER_MANAGER"

    @staticmethod
    def get_default() -> UpdateAccountInfoProcesserManager:
        return UpdateAccountInfoProcesserManager([UpdateAccountInfoProcesser])
