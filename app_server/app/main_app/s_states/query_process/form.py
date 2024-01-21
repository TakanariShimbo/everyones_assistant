from typing import Optional

from pydantic import BaseModel, ValidationError, Field

from model import AssistantTypeEntity


class Form(BaseModel):
    assistant_id: str 
    provider_id: str
    ai_model_id: str
    prompt: str = Field(min_length=1)

    @classmethod
    def from_entity(cls, assistant_entity: Optional[AssistantTypeEntity], prompt: str) -> "Form":
        if not assistant_entity:
            raise ValidationError("AssistantTypeEntity is None.")
        return cls(
            assistant_id=assistant_entity.assistant_id, 
            provider_id=assistant_entity.provider_id, 
            ai_model_id=assistant_entity.ai_model_id, 
            prompt=prompt,
        )
