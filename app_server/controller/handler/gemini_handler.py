from typing import Callable, List, Optional

from google.generativeai import configure, GenerativeModel
from google.generativeai.types import GenerateContentResponse, ContentDict


def convert_entity_to_content_dict(role: str, content: str) -> ContentDict:
    if role == "user":
        return ContentDict(role="user", parts=[content])
    elif role == "assistant":
        return ContentDict(role="model", parts=[content])
    elif role == "system":
        return ContentDict(role="user", parts=[content])
    else:
        raise ValueError("role is 'user' or 'assistant' or 'system'")


class GeminiHandler:
    @staticmethod
    def set_api_key(api_key: str) -> None:
        configure(api_key=api_key)

    @classmethod
    def query_streamly_answer_and_display(
        cls,
        prompt: str,
        ai_model_id: str = "gemini-pro",
        content_dicts: Optional[List[ContentDict]] = None,
        callback_func: Callable[[str], None] = print,
    ) -> str:
        streamly_answer = cls.query_streamly_answer(prompt=prompt, ai_model_id=ai_model_id, content_dicts=content_dicts)
        answer = cls.display_streamly_answer(streamly_answer=streamly_answer, callback_func=callback_func)
        return answer

    @classmethod
    def query_streamly_answer(
        cls,
        prompt: str,
        ai_model_id: str = "gemini-pro",
        content_dicts: Optional[List[ContentDict]] = None,
    ) -> GenerateContentResponse:
        generative_model = GenerativeModel(model_name=ai_model_id)
        chat_session = generative_model.start_chat(history=content_dicts)
        streamly_answer = chat_session.send_message(content=prompt, stream=True)
        return streamly_answer

    @staticmethod
    def display_streamly_answer(
        streamly_answer: GenerateContentResponse,
        callback_func: Callable[[str], None] = print,
    ):
        answer = ""
        for chunk in streamly_answer:
            answer_peace = chunk.text or ""
            answer += answer_peace
            callback_func(answer)
        return answer
