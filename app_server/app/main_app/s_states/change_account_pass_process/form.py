from typing import Any, Dict

from pydantic import BaseModel, ValidationError, Field


class Form(BaseModel):
    account_id: str
    current_raw_password: str = Field(min_length=4)
    new_raw_password: str = Field(min_length=4)

    @classmethod
    def init(cls, account_id: str, kwargs: Dict[str, Any]) -> "Form":
        if kwargs["new_raw_password"] != kwargs["new_raw_password_confirm"]:
            raise ValidationError("Passwords do not match.")
        
        required_dict = {}
        for name in cls.model_fields.keys():
            if name == "account_id":
                required_dict[name] = account_id
                continue
            required_dict[name] = kwargs[name]
        return cls(**required_dict)
