import pygame
class Card:
    colors = {'white':(255,255,255),
              'grey':(50,50,50),
              'red':(255,0,0)}
    
    size = (130,180)
    w = size[0]
    h = size[1]

    def __init__(self,screen,card_dict,pos=(0,0)):
        self.card_dict = card_dict

        self.screen = screen
        self.card_img = card_dict['surface']
        self.surface = pygame.image.load('assets/'+self.card_img)
        self.surface = pygame.transform.scale(self.surface, Card.size)


        self.card = card_dict['card_value']
        self.card_no = self.card[0]
        self.suit = self.card[1]
        self.card_value = self.calc_card_val()
         
        self.x = pos[0]
        self.y = pos[1]
        
        self.card_rect = pygame.Rect(self.x - 5, self.y - 4, Card.w + 10, Card.h + 8)
        self.selected = False
    
    def calc_card_val(self):
        if self.suit == 'S':
            return self.card_no
        elif self.card_no == 1:
            return 1
        elif self.card_no == 10 and self.suit == 'D':
            return 6
        else:
            return 0

    def draw(self):
        pygame.draw.rect(self.screen,Card.colors['white'],self.card_rect)
        self.screen.blit(self.surface,(self.x,self.y))
        pygame.draw.rect(self.screen,Card.colors['white'],self.card_rect,2)

    def set_pos(self,pos):
        self.pos = pos
        self.x = pos[0]
        self.y = pos[1]
        self.card_rect = pygame.Rect(self.x - 5, self.y - 4, Card.w + 10, Card.h + 8)
        

    def event_handler(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.card_rect.collidepoint(event.pos):
                    if self.selected == False:
                        pygame.draw.rect(self.screen,Card.colors['red'],self.card_rect,2)
                        self.selected = True
                        return self
                    else:
                        self.draw()
                        self.selected = False
    def __str__(self):
        return str(self.card)             

class Ghar:
    dist = 30
    def __init__(self,screen,card_list,pos=(40,40)):
        self.screen = screen
        self.card_list = card_list
        self.pos = pos
        self.x = pos[0]
        self.y = pos[1]
        if isinstance(self.card_list[0],Card):
            pass
        else:
            self.card_list = self.convert_to_card_obj()
        self.ghar_rect = pygame.Rect(self.x-5,self.y-4,((len(self.card_list)-1)*Ghar.dist)+Card.w+10,Card.h+8)

    def convert_to_card_obj(self):
        card_objs = []
        for card in self.card_list:
            card_objs.append(Card(self.screen,card))
        return card_objs
    
    def draw(self):
        for card in self.card_list:
            card.set_pos((self.x,self.y))
            card.draw()
            self.x += Ghar.dist
    
    def set_ghar_pos(self,pos):
        self.pos = pos
        self.x = pos[0]
        self.y = pos[1]
        self.ghar_rect = pygame.Rect(self.x-5,self.y-4,((len(self.card_list)-1)*Ghar.dist)+Card.w+10,Card.h+8)

    def event_handler(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.ghar_rect.collidepoint(event.pos):
                    pygame.draw.rect(self.screen,Card.colors['red'],self.ghar_rect,2)
                    return True

    def add_card(self,new_card):
        self.card_list.append(new_card)
    
    def __str__(self):
        return str(self.card_list[0])
    
    def __repr__(self):
        return str((self.pos, self.card_list[0].card))
   
class Player_cards:
    border_height = 300
    dist = 150
    def __init__(self, screen):
        self.screen = screen
        #self.card_list = card_list


    def calc_center_cards(self,card_list):
        width = self.screen.get_width()
        cards_width = ((len(card_list)-1)*Player_cards.dist)+Card.w
        starting_x = (width - cards_width)/2
        return starting_x

    def draw_player_cards(self,card_list):
        player_cards = []
        x_coordinate = self.calc_center_cards(card_list)
        y_coordinate = (self.screen.get_height()-Player_cards.border_height)+ (Player_cards.border_height-Card.h)/2
        pygame.draw.rect(self.screen, (66, 135, 245),(0,self.screen.get_height()-Player_cards.border_height,self.screen.get_width(),Player_cards.border_height),0)
        for card in card_list:
            card.set_pos((x_coordinate,y_coordinate))
            card.draw()
            x_coordinate += self.dist        


class Table:
    def __init__(self, screen):
        self.screen = screen

    def get_table_points(self):
        start_x = 40
        start_y = 40 
        table_points = []
        for j in range(2):
            for i in range(4):
                table_points.append([start_x,start_y])
                start_x += self.screen.get_width()/4
            start_x = 40
            start_y += (self.screen.get_height()-Player_cards.border_height)/2
        return table_points

    def draw_table(self,table):
        table_points = self.get_table_points()
        for ghar,j in zip(table,table_points):
            ghar.set_ghar_pos(j)
            ghar.draw()
    