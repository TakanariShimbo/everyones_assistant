from typing import Dict, Any, Tuple, Type

from ...base import BaseProcesser, BaseProcessersManager
from model import BaseResponse, Database, AccountTable


class LoadAccountsProcesser(BaseProcesser[None]):
    def _main_process(self, inner_dict: Dict[str, Any]) -> None:
        inner_dict["table"] = AccountTable.load_from_database(database_engine=Database.ENGINE)

    def _pre_process(self, outer_dict: Dict[str, Any], inner_dict: Dict[str, Any]) -> None:
        pass

    def _post_process(self, outer_dict: Dict[str, Any], inner_dict: Dict[str, Any]) -> None:
        pass

    def _callback_process(self, content: None, outer_dict: Dict[str, Any], inner_dict: Dict[str, Any]) -> None:
        pass


class LoadAccountsProcesserResponse(BaseResponse[AccountTable]):
    pass


class LoadAccountsProcesserManager(BaseProcessersManager[LoadAccountsProcesserResponse]):
    def _pre_process_for_starting(self, **kwargs) -> Tuple[Dict[str, Any], Dict[str, Any]]:
        outer_dict = {}
        inner_dict = {}
        return outer_dict, inner_dict

    def _pre_process_for_running(self, **kwargs) -> Dict[str, Any]:
        outer_dict = {}
        return outer_dict

    def _post_process(self, outer_dict: Dict[str, Any], inner_dict: Dict[str, Any]) -> LoadAccountsProcesserResponse:
        table = inner_dict["table"]
        return LoadAccountsProcesserResponse(is_success=True, contents=table)

    @staticmethod
    def _get_response_class() -> Type[LoadAccountsProcesserResponse]:
        return LoadAccountsProcesserResponse
