from typing import Any, Dict

from pydantic import BaseModel, ValidationError, Field


class Form(BaseModel):
    account_id: str = Field(min_length=4)
    current_raw_password: str = Field(min_length=4)
    new_raw_password: str = Field(min_length=4)

    @classmethod
    def init_from_dict(cls, kwargs: Dict[str, Any]) -> "Form":
        if kwargs["new_raw_password"] != kwargs["new_raw_password_confirm"]:
            raise ValidationError("Passwords do not match.")
        required_dict = {name: kwargs[name] for name in cls.model_fields.keys()}
        return cls(**required_dict)
