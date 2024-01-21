from typing import Any, Dict

from pydantic import BaseModel, Field


class Form(BaseModel):
    account_id: str = Field(min_length=4)
    raw_password: str = Field(min_length=4)

    @classmethod
    def init(cls, kwargs: Dict[str, Any]) -> "Form":
        required_dict = {name: kwargs[name] for name in cls.model_fields.keys()}
        return cls(**required_dict)
