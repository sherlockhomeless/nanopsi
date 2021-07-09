from dataclasses import dataclass
import enum


class TypeOfNeed(enum.Enum):
    """
    Classification of motive-types; Current solution is very broad and should be more finely defined
    """
    ENERGY = enum.auto()
    PAIN_AVOIDANCE = enum.auto()
    AFFILIATION = enum.auto()
    COMPETENCE = enum.auto()
    CERTAINTY = enum.auto()


@dataclass
class Need:
    current_value: float
    set_value: float
    threshold: float
    leak: float


@dataclass
class PainAvoidance(Need):
    pass


@dataclass
class EnergyIntake(Need):
    pass


@dataclass
class Affiliation(Need):
    affection: float
    legitimacy: float
    dominance: float
    parenting: float


@dataclass
class Certainty(Need):
    exploration: float
    understanding: float
    planing: float
    ideology: float


@dataclass
class Competence(Need):
    problem_solving: float
    power: float
    control: float
