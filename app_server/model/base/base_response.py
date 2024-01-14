from abc import ABC
from typing import TypeVar, Generic, Optional


T = TypeVar('T')


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
    def contents(self) -> Optional[T]:
        return self._contents


