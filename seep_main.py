import os, random, pygame, os, sys, time, copy
from seep_database import *
from seep_classes import *
from seep_player import *

pygame.init()
screen = pygame.display.set_mode((1900, 1000))
screen.fill((43, 54, 207))
pygame.display.set_caption('SEEP')
clock = pygame.time.Clock()



player_cards = get_my_cards(screen)

player_cards_1 = player_cards[:12]
player_cards_2 = player_cards[12:]
current_cards = player_cards_1

pc = Player_cards(screen)
pc.draw_player_cards(current_cards)




ghars = get_table(screen) #retrieving cards on the table
t = Table(screen) # creating a table object
t.draw_table(ghars) # drawing the table

print(ghars)
previous_card = current_cards[0]
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # for i in current_cards:
        #     if i.event_handler(event):
        #             if previous_card != i and previous_card:
        #                 previous_card.selected = False
        #                 previous_card.draw()
        #                 #current_cards.remove(i)
        #             previous_card = i 
        for i in ghars:
            if i.event_handler(event):
                if ghars != []:
                    ghars.remove(i)
                    print(ghars)
                else:
                    print('seep')
            
    if current_cards == []:
        current_cards = player_cards_2
    
    pc.draw_player_cards(current_cards)
    t.draw_table(ghars)
    update_table(ghars)
    pygame.display.update()
    clock.tick(60)