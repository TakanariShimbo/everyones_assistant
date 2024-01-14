from .handler import JsonHandler
from .static import LottiePathList

class LoadedLottie:
    wake_up_logo = JsonHandler.load(LottiePathList.wake_up_logo)
    loading = JsonHandler.load(LottiePathList.loading)