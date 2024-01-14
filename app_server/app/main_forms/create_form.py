from typing import Optional

from pydantic import BaseModel, ValidationError, Field

from model import AccountEntity, ReleaseTypeEntity


class CreateForm(BaseModel):
    account_id: str
    title: str = Field(min_length=4)
    release_id: str

    @classmethod
    def from_entity(cls, account_entity: AccountEntity, title: str, release_entity: Optional[ReleaseTypeEntity]) -> "CreateForm":
        if not release_entity:
            raise ValidationError("ReleaseTypeEntity is None.")
        return cls(account_id=account_entity.account_id, title=title, release_id=release_entity.release_id)