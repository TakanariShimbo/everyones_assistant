from passlib.context import CryptContext


class HashHandler:
    _HASHING_METHOD = "bcrypt"
    _HASHING_CONTEXT = CryptContext(schemes=[_HASHING_METHOD], deprecated="auto")

    @classmethod
    def verify(cls, raw_contents: str, hashed_contents: str) -> bool:
        is_accepted = cls._HASHING_CONTEXT.verify(secret=raw_contents, hash=hashed_contents)
        return is_accepted

    @classmethod
    def hash(cls, raw_contents: str) -> str:
        hashed_contents = cls._HASHING_CONTEXT.hash(secret=raw_contents)
        return hashed_contents