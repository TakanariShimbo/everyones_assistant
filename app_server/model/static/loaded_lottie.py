from ..handler import JsonHandler
from .path_list import LottiePathList


class LoadedLottie:
    WAKE_UP_LOGO = JsonHandler.load(LottiePathList.WAKE_UP_LOGO)
    LOADING = JsonHandler.load(LottiePathList.LOADING)
