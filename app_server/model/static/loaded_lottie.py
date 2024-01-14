from ..handler import JsonHandler
from .path_list import LottiePathList

class LoadedLottie:
    wake_up_logo = JsonHandler.load(LottiePathList.wake_up_logo)
    loading = JsonHandler.load(LottiePathList.loading)