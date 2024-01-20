from typing import Dict, Any, Tuple, Type

from ....base import BaseProcessersManager
from model import BaseResponse, AccountTable


class LoadAccountTableProcesserResponse(BaseResponse[AccountTable]):
    pass


class LoadAccountTableProcesserManager(BaseProcessersManager[LoadAccountTableProcesserResponse]):
    def _pre_process_for_starting(self, **kwargs) -> Tuple[Dict[str, Any], Dict[str, Any]]:
        outer_dict = {}
        inner_dict = {}
        return outer_dict, inner_dict

    def _pre_process_for_running(self, **kwargs) -> Dict[str, Any]:
        outer_dict = {}
        return outer_dict

    def _post_process(self, outer_dict: Dict[str, Any], inner_dict: Dict[str, Any]) -> LoadAccountTableProcesserResponse:
        table = inner_dict["table"]
        return LoadAccountTableProcesserResponse(is_success=True, contents=table)

    @staticmethod
    def _get_response_class() -> Type[LoadAccountTableProcesserResponse]:
        return LoadAccountTableProcesserResponse
