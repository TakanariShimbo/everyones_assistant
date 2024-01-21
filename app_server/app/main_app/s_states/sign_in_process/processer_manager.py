from typing import Dict, Any, Tuple, Type

from ....base import BaseProcessersManager, EarlyStopProcessException
from .form import Form
from model import BaseResponse, AccountEntity


class ProcesserResponse(BaseResponse[AccountEntity]):
    pass


class ProcesserManager(BaseProcessersManager[ProcesserResponse]):
    def _pre_process_for_starting(self, **kwargs) -> Tuple[Dict[str, Any], Dict[str, Any]]:
        outer_dict = {}
        outer_dict["message_area"] = kwargs["message_area"]

        try:
            inner_dict = {}
            inner_dict["form"] = Form.init(kwargs=kwargs)
        except:
            raise EarlyStopProcessException(message="Please input form corectly.")
        return outer_dict, inner_dict

    def _pre_process_for_running(self, **kwargs) -> Dict[str, Any]:
        outer_dict = {}
        outer_dict["message_area"] = kwargs["message_area"]

        kwargs["message_area"].warning("Running.")
        return outer_dict

    def _post_process(self, outer_dict: Dict[str, Any], inner_dict: Dict[str, Any]) -> ProcesserResponse:
        response = inner_dict["response"]
        if not response.is_success:
            return ProcesserResponse(is_success=False, message=response.message)

        return ProcesserResponse(is_success=True, contents=response.contents)

    @staticmethod
    def _get_response_class() -> Type[ProcesserResponse]:
        return ProcesserResponse
