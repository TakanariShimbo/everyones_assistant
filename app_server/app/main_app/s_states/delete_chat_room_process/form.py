from typing import Optional

from pydantic import BaseModel, ValidationError, Field

from model import ReleaseTypeEntity


class Form(BaseModel):
    account_id: str
    title: str = Field(min_length=4)
    release_id: str

    @classmethod
    def init(cls, account_id: str, title: str, release_entity: Optional[ReleaseTypeEntity]) -> "Form":
        if not release_entity:
            raise ValidationError("ReleaseTypeEntity is None.")
        return cls(account_id=account_id, title=title, release_id=release_entity.release_id)
