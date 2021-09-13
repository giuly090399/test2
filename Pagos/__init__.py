from otree.api import *

doc = """
One player decides how to divide a certain amount between himself and the other
player.
See: Kahneman, Daniel, Jack L. Knetsch, and Richard H. Thaler. "Fairness
and the assumptions of economics." Journal of business (1986):
S285-S300.
"""


class Constants(BaseConstants):
    name_in_url = 'pagos'
    players_per_group = 2
    num_rounds = 1
    endowment = cu(100)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    Correo = models.StringField(
        blank=True
    )


# PAGES
class Agradecimiento(Page):
    pass


class Pago(Page):
    form_model = 'player'
    form_fields = ['Correo']


page_sequence = [Agradecimiento, Pago]
