from openai import OpenAI


class OpenAiHandler:
    @staticmethod
    def generate_client(api_key: str) -> OpenAI:
        return OpenAI(api_key=api_key)