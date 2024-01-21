from typing import Any, Dict

from pydantic import BaseModel, EmailStr, Field


class Form(BaseModel):
    account_id: str
    mail_address: EmailStr
    family_name_en: str = Field(min_length=1)
    given_name_en: str = Field(min_length=1)
    family_name_jp: str = Field(min_length=1)
    given_name_jp: str = Field(min_length=1)
    raw_password: str = Field(min_length=4)

    @classmethod
    def init(cls, account_id: str, kwargs: Dict[str, Any]) -> "Form":
        required_dict = {}
        for name in cls.model_fields.keys():
            if name == "account_id":
                required_dict[name] = account_id
                continue
            required_dict[name] = kwargs[name]
        return cls(**required_dict)
