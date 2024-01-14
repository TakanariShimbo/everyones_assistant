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

lottie_builder = base_builder.generate_child_builder("lotties")
table_builder = base_builder.generate_child_builder("tables")


ENV_PATH = base_builder.generate_path("env", ".env")


class LottiePathList:
    loading = lottie_builder.generate_path("loading.json")
    wake_up_logo = lottie_builder.generate_path("wake_up_logo_streamlit.json")


class TablePathList:
    assistant = table_builder.generate_path("assistant.csv")
    main_component = table_builder.generate_path("main_component.csv")
    management_component = table_builder.generate_path("management_component.csv")
    provider = table_builder.generate_path("provider.csv")
    release = table_builder.generate_path("release.csv")
    role = table_builder.generate_path("role.csv")