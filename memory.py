from needs import *


class EventSchemata:
    def __init__(self, need_modification: float, need: TypeOfNeed = TypeOfNeed.ENERGY):
        raise NotImplementedError


class ActionPlan:
    def __init__(self, value_success: float = 0.0, success_probability: float = 0.0,
                 need: TypeOfNeed = TypeOfNeed.ENERGY, description: str = ""):
        self.value_success = value_success
        self.success_probability = success_probability
        self.type_need = need
        self.description = description
