import enum

class TypeOfMotives(enum.Enum):
    FOOD

class Motive:
    def __init__(self, value_of_success: float, type_of_task: str = ""):
        self.value_of_success = value_of_success
        self.motive_strength: float = 0
        self.selected_motive: bool = False
        self.type_of_task: str = type_of_task

    def update_motive_strength(self, need_indicator: float, competence_indicator: float,
                               inhibition_threshold: float = 0) -> float:
        self.motive_strength = need_indicator * self.value_of_success * competence_indicator + inhibition_threshold
        return self.motive_strength

    def __lt__(self, other):
        return self.motive_strength < other.motive_strength

