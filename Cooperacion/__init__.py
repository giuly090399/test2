import random

from otree.api import *

doc = """
One player decides how to divide a certain amount between himself and the other
player.
See: Kahneman, Daniel, Jack L. Knetsch, and Richard H. Thaler. "Fairness
and the assumptions of economics." Journal of business (1986):
S285-S300.
"""


class Constants(BaseConstants):
    name_in_url = 'cooperation'
    players_per_group = 2
    num_rounds = 4
    endowment = cu(100)


class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly(fixed_id_in_group=True)


class Group(BaseGroup):
    coop = models.CurrencyField(
        doc="""Monto que decide contribuir""",
        min=0,
        max=Constants.endowment,
        label="Contribuyo con",
    )


class Player(BasePlayer):
    pass


# PAGES
class Introduction(Page):
    pass


class Cooperacion(Page):
    form_model = 'group'
    form_fields = ['coop']
    timeout_seconds = 120

    def vars_for_template(self):
        if self.id_in_subsession % 2 == 0:
            info = 'si'
            return dict(
                info=info
            )
        else:
            info = 'no'
            return dict(
                info=info
            )


page_sequence = [Introduction, Cooperacion]
