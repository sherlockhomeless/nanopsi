from needs import *
from typing import List, Tuple, Dict
from pleasure_system import PleasureSignal
from memory import *
from event import Event
from motive import Motive
from needs import *


class PSI:
    def __init__(self, pain_avoidance: PainAvoidance, energy_intake: EnergyIntake, affiliation: Affiliation,
                 certainty: Certainty, competence: Competence,
                 need_weights: Tuple[float, float, float, float, float],
                 modulators: Tuple[float, float, float, float],
                 epistemic_competences=None,
                 motives: List[Motive] = None):
        if epistemic_competences is None:
            epistemic_competences = {}
        self.pain_avoidance = pain_avoidance
        self.energy_intake = energy_intake
        self.affiliation = affiliation
        self.competence = competence
        self.certainty = certainty
        self.epistemic_competences: Dict[str:float] = epistemic_competences

        self.needs = [self.pain_avoidance, self.energy_intake, self.affiliation, self.competence, self.certainty]
        self.need_weights = need_weights

        self.resolution = modulators[0]
        self.arousal = modulators[1]
        self.background_checks = modulators[2]
        self.inhib_threshold = modulators[3]

        self.motives = motives

        # pleasures
        self.pleasures: List[PleasureSignal] = []
        self.displeasures: List[PleasureSignal] = []
        # event schemata
        self.event_schematas: List[EventSchemata] = []
        self.action_plans: List[ActionPlan] = []
        # handle special case competence indicator
        # TODO: Add special case for need indicator method to call update_competence_indicator
        self.competence_indicator: float = 0.0
        self.update_competence_indicator(self.competence.current_value, self.motives[0])

        self.cur_motive = None
        self.select_motive()

        self.event_counter: int = 0

    def calculate_need_indicators(self, urgency=(0.0, 0.0, 0.0, 0.0, 0.0)) -> Tuple[float,...]:

        deviations = tuple(map(lambda need: need.set_value - need.current_value, self.needs))
        dev_weighted = tuple([deviations[i] * self.need_weights[i] for i in range(len(deviations))])
        need_indicators = tuple([dev_weighted[i] + urgency[i] for i in range(len(dev_weighted))])

        return need_indicators

    def update_competence_indicator(self, general_competence: float, current_motive: Motive):
        """
        :param general_competence: Value of competence tank
        :param current_motive: Currently active motive
        :return:
        """
        type_of_task: TypeOfNeed = current_motive.action_plan
        epistemic_competence = self.epistemic_competences[type_of_task]
        self.competence_indicator = general_competence + epistemic_competence
        return self.competence_indicator

    def update_modulators(self):
        """
        TODO: Include
        """
        pass

    def select_motive(self):
        for motive in self.motives:
            if motive.selected_motive:
                motive.update_motive_strength(self.competence_indicator, self.competence_indicator, inhibition_threshold=0)
            else:
                motive.update_motive_strength(self.competence_indicator, self.competence_indicator,
                                              inhibition_threshold=self.inhib_threshold)
        self.motives = self.motives.sort()

        for i in range(len(self.motives)):
            self.motives[i].selected_motive = True if i == 0 else False
        self.cur_motive = self.motives[0]

    def process_event(self, event: Event):

        def print_stats():
            need_stat = self.get_needs_printable()
            mod_stat = self.get_modulators_printable()
            print(f'{self.event_counter}: Needs={need_stat} Mods={mod_stat}')

        print(f'{self.event_counter}: {event.description}')
        for i in range(5):
            self.needs[i].current_value += event.need_dif[i]
        need_indicator = self.calculate_need_indicators()
        print_stats()

    def get_needs_printable(self) -> str:
        s: str = f'({self.pain_avoidance}\n {self.energy_intake}\n {self.affiliation}\n ' \
                 f'{self.competence}\n {self.certainty}\n'
        return s

    def get_modulators_printable(self) -> str:
        s: str = f'[ar:{self.arousal} , res:{self.resolution} ,' \
                 f' back:{self.background_checks} , inhib: {self.inhib_threshold}]'
        return s




