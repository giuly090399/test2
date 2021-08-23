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
    num_rounds = 1
    endowment = cu(100)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    coop = models.CurrencyField(
        doc="""Amount dictator decided to keep for himself""",
        min=0,
        max=Constants.endowment,
        label="Contribuyo con",
    )


class Player(BasePlayer):
    pass


# FUNCTIONS
def set_payoffs(group: Group):
    p1 = group.get_player_by_id(1)
    p2 = group.get_player_by_id(2)
    p1.payoff = group.kept
    p2.payoff = Constants.endowment - group.kept


# PAGES
class Introduction(Page):
    pass


class Cooperacion(Page):
    form_model = 'group'
    form_fields = ['coop']


page_sequence = [Introduction, Cooperacion]
