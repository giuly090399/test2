from otree.api import *


class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = 2
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    A1 = models.BooleanField(
        choices=[['Sí', 'Sí'], ['No', 'No']],
        widget=widgets.RadioSelectHorizontal
    )
    A2 = models.BooleanField(
        choices=[['Sí', 'Sí'], ['No', 'No']],
        widget=widgets.RadioSelectHorizontal
    )
    A3 = models.BooleanField(
        choices=[['Sí', 'Sí'], ['No', 'No']],
        widget=widgets.RadioSelectHorizontal
    )
    A4 = models.BooleanField(
        choices=[['Sí', 'Sí'], ['No', 'No']],
        widget=widgets.RadioSelectHorizontal
    )
    A5 = models.BooleanField(
        choices=[['Sí', 'Sí'], ['No', 'No']],
        widget=widgets.RadioSelectHorizontal
    )
    A6 = models.BooleanField(
        choices=[['Sí', 'Sí'], ['No', 'No']],
        widget=widgets.RadioSelectHorizontal
    )
    A7 = models.BooleanField(
        choices=[['Sí', 'Sí'], ['No', 'No']],
        widget=widgets.RadioSelectHorizontal
    )
    A8 = models.BooleanField(
        choices=[['Sí', 'Sí'], ['No', 'No']],
        widget=widgets.RadioSelectHorizontal
    )
    A9 = models.BooleanField(
        choices=[['Sí', 'Sí'], ['No', 'No']],
        widget=widgets.RadioSelectHorizontal
    )
    P1 = models.StringField(
        label='¿...?',
        choices=[['1', '1'], ['2', '2']]
    )
    P2 = models.StringField(
        label='¿...?',
        choices=[['1', '1'], ['2', '2']]
    )
    P3 = models.StringField(
        label='¿...?',
        choices=[['1', '1'], ['2', '2']]
    )
    OP1 = models.BooleanField(
        choices=[['Sí', 'Sí'], ['No', 'No']],
        widget=widgets.RadioSelectHorizontal
    )
    OP2 = models.BooleanField(
        choices=[['Sí', 'Sí'], ['No', 'No']],
        widget=widgets.RadioSelectHorizontal
    )
    OP3 = models.BooleanField(
        choices=[['Sí', 'Sí'], ['No', 'No']],
        widget=widgets.RadioSelectHorizontal
    )
    OP4 = models.BooleanField(
        choices=[['Sí', 'Sí'], ['No', 'No']],
        widget=widgets.RadioSelectHorizontal
    )
    OP5 = models.BooleanField(
        choices=[['Sí', 'Sí'], ['No', 'No']],
        widget=widgets.RadioSelectHorizontal
    )
    OP6 = models.BooleanField(
        choices=[['Sí', 'Sí'], ['No', 'No']],
        widget=widgets.RadioSelectHorizontal
    )
    OP7 = models.BooleanField(
        choices=[['Sí', 'Sí'], ['No', 'No']],
        widget=widgets.RadioSelectHorizontal
    )
    OP8 = models.BooleanField(
        choices=[['Sí', 'Sí'], ['No', 'No']],
        widget=widgets.RadioSelectHorizontal
    )
    OP9 = models.BooleanField(
        choices=[['Sí', 'Sí'], ['No', 'No']],
        widget=widgets.RadioSelectHorizontal
    )
    OP10 = models.BooleanField(
        choices=[['Sí', 'Sí'], ['No', 'No']],
        widget=widgets.RadioSelectHorizontal
    )
    OP11 = models.BooleanField(
        choices=[['Sí', 'Sí'], ['No', 'No']],
        widget=widgets.RadioSelectHorizontal
    )


# FUNCTIONS
# PAGES
class Instructions(Page):
    pass


class Articulos(Page):
    form_model = 'player'
    form_fields = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9']


class Preguntas(Page):
    form_model = 'player'
    form_fields = ['P1', 'P2', 'P3']


class OP1(Page):
    form_model = 'player'
    form_fields = ['OP1']


class OP1(Page):
    form_model = 'player'
    form_fields = ['OP1']


class OP2(Page):
    form_model = 'player'
    form_fields = ['OP2']


class OP3(Page):
    form_model = 'player'
    form_fields = ['OP3']


class OP4(Page):
    form_model = 'player'
    form_fields = ['OP4']


class OP5(Page):
    form_model = 'player'
    form_fields = ['OP5']


class OP6(Page):
    form_model = 'player'
    form_fields = ['OP6']


class OP7(Page):
    form_model = 'player'
    form_fields = ['OP7']


class OP8(Page):
    form_model = 'player'
    form_fields = ['OP8']


class OP9(Page):
    form_model = 'player'
    form_fields = ['OP9']


class OP10(Page):
    form_model = 'player'
    form_fields = ['OP10']


class OP11(Page):
    form_model = 'player'
    form_fields = ['OP11']


class Wait(WaitPage):
    wait_for_all_groups = True
    title_text = 'Página de espera'
    body_text = 'Por favor no salgas del experimento, la página continuará automáticamente una vez que los otros participantes hayan subido su respuesta.'


page_sequence = [Instructions, OP1, OP2, OP3, OP4, OP5, OP6, OP7, OP8, OP9, OP10, OP11, Wait]
