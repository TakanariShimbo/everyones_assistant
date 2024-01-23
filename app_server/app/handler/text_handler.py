

class TextHandler:
    @staticmethod
    def truncate(text: str, max_length: int = 22) -> str:
        return text if len(text) <= max_length else text[:max_length] + "..."