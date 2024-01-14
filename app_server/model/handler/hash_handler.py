from passlib.context import CryptContext


HASHING_METHOD = "bcrypt"
HASHING_CONTEXT = CryptContext(schemes=[HASHING_METHOD], deprecated="auto")

class HashHandler:
    @staticmethod
    def verify(raw_contents: str, hashed_contents: str) -> bool:
        is_accepted = HASHING_CONTEXT.verify(secret=raw_contents, hash=hashed_contents)
        return is_accepted

    @staticmethod
    def hash(raw_contents: str) -> str:
        hashed_contents = HASHING_CONTEXT.hash(secret=raw_contents)
        return hashed_contents