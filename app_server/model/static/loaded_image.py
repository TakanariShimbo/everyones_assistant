from ..handler import ImageHandler
from .pathes import ImagePathes


class LoadedImage:
    WAKE_UP_LOGO = ImageHandler.read_image(image_path=ImagePathes.LOGO)
