from typing import Dict, Any, Tuple, Type

from ....base import BaseProcesserManager
from ..loaded_account_table import LoadedAccountTable
from model import BaseResponse


class ProcesserResponse(BaseResponse[None]):
    pass


class ProcesserManager(BaseProcesserManager[ProcesserResponse]):
    def _pre_process_for_starting(self, **kwargs) -> Tuple[Dict[str, Any], Dict[str, Any]]:
        outer_dict = {}
        inner_dict = {}
        inner_dict["edited_display_df"] = kwargs["edited_display_df"]
        inner_dict["table"] = LoadedAccountTable.get()
        return outer_dict, inner_dict

    def _pre_process_for_running(self, **kwargs) -> Dict[str, Any]:
        outer_dict = {}
        return outer_dict

    def _post_process(self, outer_dict: Dict[str, Any], inner_dict: Dict[str, Any]) -> ProcesserResponse:
        return ProcesserResponse(is_success=True)

    @staticmethod
    def _get_response_class() -> Type[ProcesserResponse]:
        return ProcesserResponse
