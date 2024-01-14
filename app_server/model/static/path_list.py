import os


BASE_DIR = os.path.dirname(__file__)
LOTTIE_DIR = os.path.join(BASE_DIR, "lotties")
TABLE_DIR = os.path.join(BASE_DIR, "tables")


class LottiePathList:
    loading = os.path.join(LOTTIE_DIR, "loading.json")
    wake_up_logo = os.path.join(LOTTIE_DIR, "wake_up_logo_streamlit.json")


class TablePathList:
    assistant = os.path.join(TABLE_DIR, "assistant.csv")
    main_component = os.path.join(TABLE_DIR, "main_component.csv")
    management_component = os.path.join(TABLE_DIR, "management_component.csv")
    provider = os.path.join(TABLE_DIR, "provider.csv")
    release = os.path.join(TABLE_DIR, "release.csv")
    role = os.path.join(TABLE_DIR, "role.csv")