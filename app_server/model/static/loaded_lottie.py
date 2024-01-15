from ..handler import JsonHandler
from .pathes import LottiePathes


class LoadedLottie:
    WAKE_UP_LOGO = JsonHandler.load(LottiePathes.WAKE_UP_LOGO)
    LOADING = JsonHandler.load(LottiePathes.LOADING)
