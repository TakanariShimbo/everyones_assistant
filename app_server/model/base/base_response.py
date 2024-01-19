from abc import ABC
from typing import TypeVar, Generic, Optional


T = TypeVar("T")


class BaseResponse(Generic[T], ABC):
    def __init__(self, is_success: bool, message: str = "", contents: Optional[T] = None) -> None:
        self._is_success = is_success
        self._message = message
        self._contents = contents

    @property
    def is_success(self) -> bool:
        return self._is_success

    @property
    def message(self) -> str:
        return self._message

    @property
    def contents(self) -> T:
        contents = self._contents
        if contents == None:
            raise ValueError("Not accessible due to have not constracted.")
        return contents
