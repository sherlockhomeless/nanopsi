from agent import PSI, Event
from needs import *
from pleasure_system import *
from typing import *
from motive import Motive


def start_script():


    psi = create_agent()

    # add relevant event schemata
    bear_aversion = NotImplementedError

    event_loop: List[Event] = []
    # psi agent gathers wood for fire
    event_description = "Agent is calmly collecting wood for a fire in the forest, all tanks full"
    need_dif = (0, 0, 0, 0, 0)
    wood_gathering = Event(event_description, need_dif, PleasureSignal(True, EnergyIntake, None))

    event_loop.append(wood_gathering)
    # psi agent
    for event in event_loop:
        psi.process_event(event)


def create_agent():
    # --- setup needs ---
    # (current value, set value, threshold, leak)
    pain_avoidance: PainAvoidance = PainAvoidance(0.7, 0.8, 0.1, 0.00)
    energy_intake: EnergyIntake = EnergyIntake(0.9, 0.7, 0.5, 0.01)
    affiliation: Affiliation = Affiliation(0.8, 0.6, 0.4, 0.01, 0.8, 0.8, 0.5, -1)
    competence: Competence = Competence(0.9, 0.6, 0.4, 0.05, 0.9, 0.7, 0.8)
    certainty: Certainty = Certainty(0.9, 0.7, 0.5, 0.05, 0.95, 0.9, 0.9, 0.8)
    need_weights = (3.0, 3.0, 2.0, 2.5, 2.0)

    # --- setup modulators ---
    resolution = 0.3
    arousal = 0.3
    background_checks = 0.4
    inhib_threshold = 0.5
    modulators = (resolution, arousal, background_checks, inhib_threshold)

    # --- setup epistemic knowledge ---
    # epistemic knowledge
    epistemic_competence = {
        'hunting': 0.3,
        'cook_food': 0.4,
        'fight': 0.3,
        'wood_working': 0.5
    }

    # --- setup motives ---
    motives: List[Motive, ...] = []
    motive_food = Motive(0.9, '')
    motive_sleep =

    psi = PSI(pain_avoidance, energy_intake, affiliation, certainty, competence, need_weights, modulators,
              epistemic_competences=epistemic_competence, motives=motives)
    return psi


if __name__ == '__main__':
    start_script()
