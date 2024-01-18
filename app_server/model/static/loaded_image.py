from ..handler import ImageHandler
from .pathes import ImagePathes


class LoadedImage:
    LOGO = ImageHandler.read_image_depth32(image_path=ImagePathes.LOGO)
