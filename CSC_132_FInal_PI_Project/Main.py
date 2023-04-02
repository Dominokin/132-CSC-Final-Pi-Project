from random import randint
import pygame
from time import *
from Player import *
from Enemy import *
from Sprite import *

##################  GAME CLASS SETUP  ##################
class Game(Player, Sprite):
    def __init__(self, enc_num):
        super().__init__()
        self.enc_num = enc_num

    @property
    def enc_num(self):
        return self._enc_num

    @enc_num.setter
    def enc_num(self, value):
        self._enc_num = value

    #scale enemy health and damage. Can be adjusted later
    def scale(self):
        scale_amount = enc_num * .5
        Enemy.health *= scale_amount
        Enemy.damage *= scale_amount

    #mini boss encounter after 4 to 6 rounds
    def mini_boss_enc(self):
        if self.enc_num == 4 and self.enc_num < 6:
            choose = randint(0,100)
            if choose > 50:
                #start mini boss encounter
                pass
        elif self.enc_num == 6:
            #start mini boss encounter no matter what
            #also find a way where after 2 mini boss encounter, goes back
            #to normal encounters 4-6 times, then goes to actual boss
            pass

######################## THIS IS THE SETUP FOR MAIN GAME LOOP #######################

pygame.init()

#set the frame rate for animations
clock = pygame.time.Clock()
fps = 30

#set the area for the bottom pannel to display character's stuff
bottom_pannel = 150
#define screen dimentions
screen_width = 1000
screen_height = 600 + bottom_pannel


#set up the display
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pi game")

##load images and use functions for drawing them onto the screen
##### THIS WILL BE SET LATER ##########


######################## THIS IS THE MAIN GAME LOOP #######################
running = True
while(running):
    #checking for exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #set frame rate
    clock.tick(fps)

    #draw the background
    #TBD
    
    #start the game
    pygame.display.update()
pygame.quit()
