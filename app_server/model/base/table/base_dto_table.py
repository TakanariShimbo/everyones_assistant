from abc import ABC
from typing import TypeVar

from ..config import BaseDtoConfig
from ..bean import BaseDto
from .base_table import BaseTable


C = TypeVar("C", bound=BaseDtoConfig)
B = TypeVar("B", bound=BaseDto)
T = TypeVar("T", bound="BaseDtoTable")


class BaseDtoTable(BaseTable[C, B], ABC):
    pass