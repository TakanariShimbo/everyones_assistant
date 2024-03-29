import os


class PathBuilder:
    def __init__(self, base_dir: str):
        self.base_dir = base_dir

    def generate_path(self, *segments: str) -> str:
        return os.path.join(self.base_dir, *segments)

    def generate_child_builder(self, *segments: str) -> "PathBuilder":
        new_base_dir = self.generate_path(*segments)
        return PathBuilder(base_dir=new_base_dir)


base_dir = os.path.dirname(__file__)
base_builder = PathBuilder(base_dir=base_dir)

image_builder = base_builder.generate_child_builder("images")
lottie_builder = base_builder.generate_child_builder("lotties")
table_builder = base_builder.generate_child_builder("tables")


ENV_PATH = base_builder.generate_path("env", ".env")


class ImagePathes:
    LOGO = image_builder.generate_path("logo_streamlit.png")


class LottiePathes:
    LOADING = lottie_builder.generate_path("loading.json")
    WAKE_UP_LOGO = lottie_builder.generate_path("wake_up_logo_streamlit.json")


class TablePathes:
    ASSISTNAT = table_builder.generate_path("assistant.csv")
    MAIN_COMPONENT = table_builder.generate_path("main_component.csv")
    MANAGEMENT_COMPONENT = table_builder.generate_path("management_component.csv")
    PROVIDER = table_builder.generate_path("provider.csv")
    RELEASE = table_builder.generate_path("release.csv")
    ROLE = table_builder.generate_path("role.csv")