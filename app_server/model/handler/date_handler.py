from typing import Optional, Union
from datetime import datetime


class DateHandler:
    @staticmethod
    def to_str(date: Union[str, datetime]) -> str:
        if isinstance(date, datetime):
            return str(date)
        elif isinstance(date, str):
            return date
        else:
            raise ValueError("date must be 'str', 'datetime'.")

    @staticmethod
    def to_str_or_none(date: Optional[Union[str, datetime]]) -> Optional[str]:
        if isinstance(date, datetime):
            return str(date)
        elif isinstance(date, str) or date == None:
            return date
        else:
            raise ValueError("date must be 'str', 'datetime', or 'None'.")