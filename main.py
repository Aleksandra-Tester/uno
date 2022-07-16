from enum import Enum

colour = ['RED','GREEN','BLUE','YELLOW']
value = ['0','1','2','3','4','5','6','7','8','9','Skip','Reverse','Draw2','Draw4','Chance_colour']
type = {'0':'number','1':'number','2':'number','3':'number','4':'number','5':'number','6':'number',
        '7':'number','8':'number','9':'number','Skip':'action','Reverse':'action','Draw2':'action',
        'Draw4':'action_nocolour','Change_colour':'action_nocolour'}

class Card:
    def __init__(self, colour, value, type):
        self.colour = colour
        self.value = value
        self.type = type

class TextEnum(Enum):
    @property
    def description(self):
        return self.value[1]

class Actions(TextEnum):
    SKIP = 0,"Next player in sequence misses a turn."
    REVERSE = 1,"Order of play switches directions."
    DRAW2 = 2,"Next player in sequence draws two cards and misses a turn."
    DRAW4 = 3,"Player declares the next colour to be matched; next player in sequence draws four cards and misses a turn."
    CHANGE_COLOUR = 4,"Player declares the next colour to be matched."

for actions in Actions:
    print (actions.description)

red_5 = Card("RED",5,None)
red_skip = Card("RED",None,Actions.SKIP)
