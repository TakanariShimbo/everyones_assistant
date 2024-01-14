

BASE_DIR = "./model/static/"
LOTTIE_DIR = BASE_DIR + "lotties/"
TABLE_DIR = BASE_DIR + "tables/"


class LottiePathList:
    loading = LOTTIE_DIR + "loading.json"
    wake_up_logo = LOTTIE_DIR + "wake_up_logo_streamlit.json"


class TablePathList:
    assistant = TABLE_DIR + "assistant.csv"
    main_conponennt = TABLE_DIR + "main_conponent.csv"
    management_conponennt = TABLE_DIR + "management_conponent.csv"
    provider = TABLE_DIR + "provider.csv"
    release = TABLE_DIR + "release.csv"
    role = TABLE_DIR + "role.csv"