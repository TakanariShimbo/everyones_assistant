from ..handler import ImageHandler
from .pathes import ImagePathes


class LoadedImage:
    LOGO = ImageHandler.read_image(image_path=ImagePathes.LOGO)
