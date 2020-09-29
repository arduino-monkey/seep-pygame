import pyrebase
from seep_classes import *
from seep_player import *
from seep_database_config import *

firebase  = pyrebase.initialize_app(config)
db = firebase.database()


def get_my_cards(screen):
    lis = db.child('game').child(player).get().val()['cards']
    card_objs = []
    for card in lis:
        card_objs.append(Card(screen,card))
    return card_objs

def get_table(screen):
    try:
        lis = db.child('game').child('table').get().val()['cards']
        ghar_objs = []
        for ghar in lis:
            ghar_objs.append(Ghar(screen,ghar))
        return ghar_objs
    except TypeError:
        return []

def update_table(ghars):
    lis = []
    for ghar in ghars:
        temp = []
        for card in ghar.card_list:
            temp.append(card.card_dict)
        lis.append(temp)
    table = {'cards':lis}
    db.child('game').child('table').update(table) 

