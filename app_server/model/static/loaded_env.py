import os

from dotenv import load_dotenv

from .path_list import ENV_PATH


load_dotenv(dotenv_path=ENV_PATH)


class LoadedEnv:
    ADMIN_ID = os.environ["ADMIN_ID"]
    ADMIN_PASSWORD = os.environ["ADMIN_PASSWORD"]
    DATABASE_TYPE = os.environ["DATABASE_TYPE"]
    DATABASE_USER = os.environ["DATABASE_USER"]
    DATABASE_PASSWORD = os.environ["DATABASE_PASSWORD"]
    DATABASE_HOST = os.environ["DATABASE_HOST"]
    DATABASE_PORT = os.environ["DATABASE_PORT"]
    DATABASE_DB = os.environ["DATABASE_DB"]
    OPEN_AI_API_KEY = os.environ["OPEN_AI_API_KEY"]
    GEMINI_API_KEY = os.environ["GEMINI_API_KEY"]
