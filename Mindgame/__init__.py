from otree.api import *
import random


class Constants(BaseConstants):
    name_in_url = 'mindgame'
    players_per_group = 2
    num_rounds = 1
    endowment = cu(100)
    num = random.choice([1, 2, 3, 4, 5, 6])


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    dado = models.BooleanField(
        choices=[['True', 'Sí'], ['False', 'No']]
    )


class Player(BasePlayer):
    pass


# PAGES
class Introduction2(Page):
    pass


class Dado(Page):
    pass


class Dado2(Page):
    form_model = 'group'
    form_fields = ['dado']
    timeout_seconds = 120


class Wait(WaitPage):
    wait_for_all_groups = True
    title_text = 'Página de espera'
    body_text = 'Por favor no salgas del experimento, la página continuará automáticamente una vez que los otros participantes hayan subido su respuesta.'


page_sequence = [Introduction2, Dado, Dado2, Wait]
