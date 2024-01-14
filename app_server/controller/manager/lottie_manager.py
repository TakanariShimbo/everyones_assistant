from ..handler import JsonHandler

class LottieManager:
    WAKE_UP_LOGO = JsonHandler.load("./static/lotties/wake_up_logo_streamlit.json")
    LOADING = JsonHandler.load("./static/lotties/loading.json")