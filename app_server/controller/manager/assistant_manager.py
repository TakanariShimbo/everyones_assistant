from typing import Callable, List

from ..handler import ChatGptHandler, convert_entity_to_message_param, GeminiHandler, convert_entity_to_content_dict
from model import ChatMessageEntity, PROVIDER_TYPE_TABLE, LoadedEnv


class AssistantManager:
    client = ChatGptHandler.generate_client(api_key=LoadedEnv.OPEN_AI_API_KEY)
    GeminiHandler.set_api_key(api_key=LoadedEnv.GEMINI_API_KEY)

    @classmethod
    def query_streamly_answer_and_display(
        cls,
        prompt: str,
        provider_id: str,
        ai_model_id: str,
        message_entities: List[ChatMessageEntity],
        callback_func: Callable[[str], None],
    ) -> str:
        if provider_id == PROVIDER_TYPE_TABLE.open_ai_id:
            return cls._query_to_open_ai(
                prompt=prompt, 
                ai_model_id=ai_model_id, 
                message_entities=message_entities, 
                callback_func=callback_func,
            )
        elif provider_id == PROVIDER_TYPE_TABLE.google_id:
            return cls._query_to_google(
                prompt=prompt, 
                ai_model_id=ai_model_id, 
                message_entities=message_entities, 
                callback_func=callback_func,
            )
        else:
            raise ValueError("provider_id must be 'open-ai' or 'google'.")

    @classmethod
    def _query_to_open_ai(
        cls,
        prompt: str,
        ai_model_id: str,
        message_entities: List[ChatMessageEntity],
        callback_func: Callable[[str], None],
    ) -> str:
        message_params = [convert_entity_to_message_param(role=message_entity.role_id, content=message_entity.content) for message_entity in message_entities]
        answer = ChatGptHandler.query_streamly_answer_and_display(
            client=cls.client,
            prompt=prompt,
            ai_model_id=ai_model_id,
            message_prams=message_params,
            callback_func=callback_func,
        )
        return answer

    @staticmethod
    def _query_to_google(
        prompt: str,
        ai_model_id: str,
        message_entities: List[ChatMessageEntity],
        callback_func: Callable[[str], None],
    ) -> str:
        content_dicts = [convert_entity_to_content_dict(role=message_entity.role_id, content=message_entity.content) for message_entity in message_entities]
        answer = GeminiHandler.query_streamly_answer_and_display(
            prompt=prompt,
            ai_model_id=ai_model_id,
            content_dicts=content_dicts,
            callback_func=callback_func,
        )
        return answer
