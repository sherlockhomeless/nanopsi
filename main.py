import needs
from agent import PSI, Event
from needs import *
from pleasure_system import *
from typing import *
from motive import *


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
    inhib_threshold = -0.2  # determines the discount for all non active motives
    modulators = (resolution, arousal, background_checks, inhib_threshold)

    # --- setup event schemata ---
    schemata: List[EventSchemata, ...] = []

    # --- setup action plans ---
    ap_gather_food = ActionPlan(description="psi gathers berries & roots to eat",
                                value_success=0.2, success_probability=0.8, need=TypeOfNeed.ENERGY)
    ap_get_food_from_storage = ActionPlan(description="psi goes to storage and picks up food", value_success=0.4,
                                          success_probability=0.8, need=TypeOfNeed.ENERGY)
    ap_sleep = ActionPlan(description="PSI does internal clean up jobs aka 'robo-sleep'", value_success=0.1,
                          success_probability=1.0, need=TypeOfNeed.ENERGY)
    ap_signal_help = ActionPlan(description="", value_success=0.0, success_probability=0.0, need=TypeOfNeed.ENERGY)
    ap_construct_ap = ActionPlan(description="", value_success=0.0, success_probability=0.0, need=TypeOfNeed.ENERGY)
    ap_explore = ActionPlan(description="", value_success=0.0, success_probability=0.0, need=TypeOfNeed.ENERGY)
    ap_flee = ActionPlan(description="", value_success=0.0, success_probability=0.0, need=TypeOfNeed.ENERGY)
    ap_fight = ActionPlan(description="", value_success=0.0, success_probability=0.0, need=TypeOfNeed.ENERGY)
    ap_group_fight = ActionPlan(description="", value_success=0.0, success_probability=0.0, need=TypeOfNeed.ENERGY)

    # --- epistemic competence ---
    epistemic_competence = {
        ap_gather_food: ap_gather_food.success_probability,
        ap_get_food_from_storage: ap_get_food_from_storage.success_probability,
        ap_sleep: ap_sleep.success_probability
    }
    # --- setup motives ---
    motive_food = Motive(0.9, TypeOfNeed.ENERGY,  )
    motive_sleep = Motive(0.3, TypeOfNeed.ENERGY)
    motive_explore = Motive(0.15, TypeOfNeed.CERTAINTY)
    motive_build_group_coherence = Motive(0.2, TypeOfNeed.AFFILIATION)

    motives: List[Motive, ...] = [motive_food, motive_sleep, motive_explore, motive_build_group_coherence]
    psi = PSI(pain_avoidance, energy_intake, affiliation, certainty, competence, need_weights, modulators,
              epistemic_competences=epistemic_competence, motives=motives)
    return psi


if __name__ == '__main__':
    start_script()
