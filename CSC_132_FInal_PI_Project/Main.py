from random import randint
import pygame
from time import *
from Player import *
from Enemy import *
#from Sprite import *

##################  GAME CLASS SETUP  ##################
class Game(Player, Enemy):
    def __init__(self):
        Player.__init__()
        Enemy.__init__()

    def draw_player(Player):
        screen.blit(Player.image, Player.rect)

    def draw_enemy(Enemy):
        screen.blit(Enemy.image, Enemy.rect)

    #scale enemy health and damage. Can be adjusted later
    def scale(self):
        scale_amount = enc_num * .5
        Enemy.health *= scale_amount
        Enemy.damage *= scale_amount

    #mini boss encounter after 4 to 6 rounds
    def mini_boss_enc(self):
        if self.enc_num == 4 and self.enc_num < 6:
            choose = randint(0,101)
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
screen_width = 785
screen_height = 442 + bottom_pannel

#set up the display
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pi game")

#load images and use functions for drawing them onto the screen
background_img = pygame.image.load('Background\dungeon-bg.jpeg').convert_alpha()
def draw_bg():
    screen.blit(background_img, (0,0))

#instantiate 
p = Player(200, 250, 30, 30, 10, 1)

#make enemy types
bat = Enemy(500, 250, "Bat", 10, 10)
witch = Enemy(500, 250, "Witch", 30, 20)
wolf = Enemy(500, 250, "Wolf", 20, 15)

#put the enemies in lists to easily randomize which one to use
enemy_list = []
enemy_list.append(bat)
enemy_list.append(witch)
enemy_list.append(wolf)

#start the encounter
enc_num = 1

#displayed number of encounters
#reset after every mini boss round
enc_count = 1

#replace the numbers with the gpio inputs
p.attack = 1
p.heal = 2
p.flee = 3

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
    draw_bg()

    #draw the player
    Game.draw_player(p)

    #spawn random enemy type
    choose_enemy = randint(0, 2)
    Game.draw_enemy(enemy_list[choose_enemy])
    
    #let player go first
    #if the player attacks, use the player.attack method in the Player class
    #if the players heals, use the player.heal method in the Player class
    #if the player flees, pass all of this and restart the encounter
    #check to see if the enemy has felled. If not, then it is the enemy's turn
    #if player doesn't flee, use the enemy attack method in the enemy class
    #check player health and if you die, play death animation
    #if the player is still alive, reset the gameplay loop
    
    #process(button):
        #if player.health == 0:
            ##Implement death function for player
            #player.die
        #if enemy.health == 0:
            ##Implement death function for enemy
            #enemy.die
        #if button == p.attack
            #player.attack()
            #enemy.attack()
        #if button == p.heal
            #player.heal()
            #enemy.attack()
        #if button == p.flee
            #player.flee()
    pygame.display.update()
pygame.quit()
