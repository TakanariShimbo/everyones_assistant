from abc import ABC
from typing import TypeVar

from ..config import BaseDtoConfig
from .base_bean import BaseBean


C = TypeVar("C", bound=BaseDtoConfig)


class BaseDto(BaseBean[C], ABC):
    pass
