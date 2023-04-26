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

##    #function to load the images for animation
##    def load(self):
##        #temp list to add to the actual list of animations
##        temp_list = []
##        #load the idle sprite sheet and put it into the temp list
##        img = pygame.image.load(f"AllCharacters/{self.name}/{self.name}Idle_strip.png")
##        temp_list.append(img)
##        #load the attack sprite sheet and put it into the temp list
##        img = pygame.image.load(f"AllCharacters/{self.name}/{self.name}Attack_strip.png")
##        temp_list.append(img)
##        #load the death sprite sheet and put it into the temp list
##        img = pygame.image.load(f"AllCharacters/{self.name}/{self.name}Death_strip.png")
##        temp_list.append(img)
##        return temp_list

    def draw_player(Player):
        screen.blit(Player.image, Player.rect)

    def draw_enemy(Enemy):
        screen.blit(Enemy.image, Enemy.rect)

    def update(self):
        animation_cooldown = 100
        #handle animation
        #update image
        self.image = self.animation_list[self.action][self.frame_index]
        #check if enough time has passed since the last update
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index = 0
        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame = 0

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

    def get_img(self, frame, width, height, scale, color):
        img = pygame.Surface((width, height)).convert_alpha()
        #This part of the method will take the following arguments, respectivly:
        #the sprite sheet instantiated by the SpriteSheet class
        #the origin on the screen it will be rendered
        #frame * width and 0 is what frame will be rendered from the sprite sheet
        #width and height is how much of the frame will be shown...
        #In this case, we want all of the image to show
        img.blit(self.image, (0, 0), ((frame * width), 0, width, height))
        img = pygame.transform.scale(self.image, (width * scale, height * scale))
        img.set_colorkey(color)
        return img

######################## THIS IS THE SETUP FOR MAIN GAME LOOP #######################

pygame.init()

#game variables
current_turn = 1
total_turns = 2
action_wait_time = 90

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
pygame.display.set_caption("Final Pi Project game thing idk")

#load images and use functions for drawing them onto the screen
background_img = pygame.image.load('Background\dungeon-bg.jpeg').convert_alpha()
def draw_bg():
    screen.blit(background_img, (0,0))

#instantiate the player
p = Player(300, 300, "Knight", 30, 30, 10, 1)

#make enemy types
#this will also load sprite sheets into its respective self.animation_list
bat = Enemy(500, 250, "Bat", 10, 10)
witch = Enemy(500, 250, "Witch", 30, 20)
wolf = Enemy(500, 250, "Wolf", 20, 15)

#put all instatntiated characters in a dict
#makes random enemies easier
#allows all sprite sheets to be loaded in for animation
sprite_dict = {0: bat, 1: witch, 2: wolf, 3:p}

#animation constants
animation_steps = {"KnightIdle": 15, "KnightAttack": 21, "KnightDeath": 15, "BatIdle": 8,\
                    "BatAttack": 10, "BatDeath": 10, "WitchIdle": 7, "WitchAttack": 18, \
                    "WitchDeath": 12, "WolfIdle": 12, "WolfAttack": 16, "WolfDeath": 18}

#master 


#for sprite in range(sprite_dict):
    #for frame in 
#instantiate the enemy
newEnemy = None

#start the encounter
enc_num = 1

#displayed number of encounters
#reset after every mini boss round
enc_count = 1

#replace the numbers with the gpio inputs
p.attack = 1
p.heal = 2
p.flee = 3
    
#Background removal color
BG_REMOVE = (113, 102, 79, 255)

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

    #spawn random enemy type
    if newEnemy == None:
        choose_enemy = randint(0, 2)
        newEnemy = sprite_dict[choose_enemy]
    Game.get_img(p, animation_steps["KnightIdle"], 64, 64, 3, BG_REMOVE)
    Game.draw_player(p)
    Game.draw_enemy(newEnemy)
    #newEnemy.update()
    

    #let player go first
    if p.current_health > 0:
        #if the player attacks, use the player.attack method in the Player class
        if p.attack:
            damage = p.attack
            newEnemy.health -= damage
        #if the players heals, use the player.heal method in the Player class
        elif p.heal:
            p.heal
            p.potions -= 1
        #if the player flees, pass all of this and restart the encounter
        elif p.flee:
            break
    #if player doesn't flee, use the enemy attack method in the enemy class
    if newEnemy.health > 0:
        enemyDamage = newEnemy.attack()
        #check player health and if you die, play death animation
        p.current_health -= enemyDamage    
    #if the player is still alive, reset the gameplay loop
        
    pygame.display.update()
pygame.quit()
