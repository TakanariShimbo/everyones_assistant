import os

from dotenv import load_dotenv

from .path_list import ENV_PATH


load_dotenv(dotenv_path=ENV_PATH)


class LoadedEnv:
    admin_id = os.environ["ADMIN_ID"]
    admin_password = os.environ["ADMIN_PASSWORD"]
    database_type = os.environ["DATABASE_TYPE"]
    database_user = os.environ["DATABASE_USER"]
    database_password = os.environ["DATABASE_PASSWORD"]
    database_host = os.environ["DATABASE_HOST"]
    database_port = os.environ["DATABASE_PORT"]
    database_db = os.environ["DATABASE_DB"]
    open_ai_api_key = os.environ["OPEN_AI_API_KEY"]
    gemini_api_key = os.environ["GEMINI_API_KEY"]
