from ...base import BaseQParamNoDefault


class ComponentId(BaseQParamNoDefault):
    @staticmethod
    def get_name() -> str:
        return "component-id"
