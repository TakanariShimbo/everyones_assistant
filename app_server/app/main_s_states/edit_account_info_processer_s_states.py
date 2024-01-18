from .edit_account_info_processers import EditAccountInfoProcesser, EditAccountInfoProcesserManager
from ..base import BaseSState


class EditAccountInfoProcesserSState(BaseSState[EditAccountInfoProcesserManager]):
    @staticmethod
    def get_name() -> str:
        return "EDIT_ACCOUNT_INFO_PROCESSER_MANAGER"

    @staticmethod
    def get_default() -> EditAccountInfoProcesserManager:
        return EditAccountInfoProcesserManager([EditAccountInfoProcesser])
