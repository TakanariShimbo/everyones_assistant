from typing import Any, Dict

from pydantic import BaseModel, EmailStr, Field


class Form(BaseModel):
    account_id: str = Field(min_length=4)
    mail_address: EmailStr
    family_name_en: str = Field(min_length=1)
    given_name_en: str = Field(min_length=1)
    family_name_jp: str = Field(min_length=1)
    given_name_jp: str = Field(min_length=1)
    raw_password: str = Field(min_length=4)

    @classmethod
    def init_from_dict(cls, kwargs: Dict[str, Any]) -> "Form":
        required_dict = {name: kwargs[name] for name in cls.model_fields.keys()}
        return cls(**required_dict)
