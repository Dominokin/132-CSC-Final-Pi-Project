from random import randint
import pygame
from time import *

##################  GAME CLASS SETUP  ##################
class Game:
    def __init__(self, x, y, name, current_health, max_health, damage, level, potions):
        self.x = x
        self.y = y
        self.name = name
        self.current_health = current_health
        self.max_health = max_health
        self.damage = damage
        self.level = level
        self.potions = potions
        self.animation_list = []
        self.frame = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()
        self.animation_cooldown = 100
        #Background removal color
        BG_REMOVE = (113, 102, 79, 255)
        self.animation_steps = {"KnightIdle": 15, "KnightAttack": 21, "KnightDeath": 15, "BatIdle": 8,\
                    "BatAttack": 10, "BatDeath": 10, "WitchIdle": 7, "WitchAttack": 18, \
                    "WitchDeath": 12, "WolfIdle": 12, "WolfAttack": 16, "WolfDeath": 18}
        #load the sprite sheets
        temp_list = []
        img = pygame.image.load(f"AllCharacters/{self.name}/{self.name}Idle_strip.png")
        #seperate them out into images and then put them in a list
        #first is the idle frames
        if self.name == "Knight":
            for x in range(self.animation_steps[f"{self.name}Idle"]):
                temp_image = self.get_img(img, x, 96, 64, 3, BG_REMOVE)
                temp_list.append(temp_image)
            self.animation_list.append(temp_list)
            #Next is the attack frames
            temp_list = []
            img = pygame.image.load(f"AllCharacters/{self.name}/{self.name}Attack_strip.png")
            for x in range(self.animation_steps[f"{self.name}Attack"]):
                temp_image = self.get_img(img, x, 144, 64, 3, BG_REMOVE)
                temp_list.append(temp_image)
            self.animation_list.append(temp_list)
            #last is the death frames
            temp_list = []
            img = pygame.image.load(f"AllCharacters/{self.name}/{self.name}Death_strip.png")
            for x in range(self.animation_steps[f"{self.name}Death"]):
                temp_image = self.get_img(img, x, 96, 64, 3, BG_REMOVE)
                temp_list.append(temp_image)
            self.animation_list.append(temp_list)
        else:
            for x in range(self.animation_steps[f"{self.name}Idle"]):
                temp_image = self.get_img(img, x, 64, 64, 3, BG_REMOVE)
                temp_list.append(temp_image)
            self.animation_list.append(temp_list)
            #Next is the attack frames
            temp_list = []
            img = pygame.image.load(f"AllCharacters/{self.name}/{self.name}Attack_strip.png")
            for x in range(self.animation_steps[f"{self.name}Attack"]):
                temp_image = self.get_img(img, x, 64, 64, 3, BG_REMOVE)
                temp_list.append(temp_image)
            self.animation_list.append(temp_list)
            #last is the death frames
            temp_list = []
            img = pygame.image.load(f"AllCharacters/{self.name}/{self.name}Death_strip.png")
            for x in range(self.animation_steps[f"{self.name}Death"]):
                temp_image = self.get_img(img, x, 64, 64, 3, BG_REMOVE)
                temp_list.append(temp_image)
            self.animation_list.append(temp_list)
        self.image = self.animation_list[self.action][self.frame]
        self.rect = self.image.get_rect(center = (self.x, self.y))

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @x.setter
    def y(self, value):
        self._y = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def max_health(self):
        return self._max_health

    @max_health.setter
    def max_health(self, value):
        self._max_health = value

    @property
    def current_health(self):
        return self._current_health

    @current_health.setter
    def current_health(self, newHealth):
        if(newHealth >= 30):
            self._current_health = 30
        elif(newHealth <= 0):
            #play the death animation
            self._action = 2
            #maybe have a screen pop up saying YOU DIED or something like that
            pass
        else:
            self._current_health = newHealth

    @property
    def damage(self):
        return self._damage

    @damage.setter
    def damage(self, value):
        self._damage = value

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value

    @property
    def potions(self):
        return self._potions

    @potions.setter
    def potions(self, value):
        self._potions = value

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value

    def draw(self):
        screen.blit(self.image, self.rect)

    def update(self):
        self.image = self.animation_list[self.action][self.frame]
        #if the time that has past since the last update is longer than the...
        #animation cooldown (100 ms)
        if pygame.time.get_ticks() - self.update_time > self.animation_cooldown:
            #update the frame and reset the recent update to the last tick
            self.update_time = pygame.time.get_ticks()
            self.frame += 1
            if self.frame >= len(self.animation_list[self.action]):
                self.frame = 0

    #scale health and damage. Can be adjusted later
    def scale(self):
        scale_amount = enc_num * .5
        self.max_health *= scale_amount
        self.damage *= scale_amount

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

    def get_img(self, image, frame, width, height, scale, color):
        temp_image = pygame.Surface((width, height)).convert_alpha()
        #This part of the method will take the following arguments, respectivly:
        #the sprite sheet instantiated by the SpriteSheet class
        #the origin on the screen it will be rendered
        #frame * width and 0 is what frame will be rendered from the sprite sheet
        #width and height is how much of the frame will be shown...
        #In this case, we want all of the image to show
        temp_image.blit(image, (0, 0), ((frame * width), 0, width, height))
        temp_image = pygame.transform.scale(temp_image, (width * scale, height * scale))
        temp_image.set_colorkey(color)
        return temp_image

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
p = Game(350, 250, "Knight", 30, 30, 10, 1, 1)

#make enemy types
#this will also load sprite sheets into its respective self.animation_list
bat = Game(400, 100, "Bat", 10, 10, 10, 1, 0)
witch = Game(400, 100, "Witch", 30, 30, 20, 1, 0)
wolf = Game(400, 100, "Wolf", 20, 20, 15, 1, 0)

#put all instatntiated characters in a dict
#makes random enemies easier
#allows all sprite sheets to be loaded in for animation
sprite_dict = {0: bat, 1: witch, 2: wolf, 3:p}

#instantiate the enemy
newEnemy = None

#start the encounter
enc_num = 1

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

    #spawn random enemy type
    if newEnemy == None:
        choose_enemy = randint(0, 2)
        newEnemy = sprite_dict[choose_enemy]
    p.update()
    p.draw()
    newEnemy.update()
    newEnemy.draw()
    

    #let player go first
##    if p.current_health > 0:
##        #if the player attacks, use the player.attack method in the Player class
##        if p.attack:
##            damage = p.attack
##            newEnemy.health -= damage
##        #if the players heals, use the player.heal method in the Player class
##        elif p.heal:
##            p.heal
##            p.potions -= 1
##        #if the player flees, pass all of this and restart the encounter
##        elif p.flee:
##            break
##    #if player doesn't flee, use the enemy attack method in the enemy class
##    if newEnemy.health > 0:
##        enemyDamage = newEnemy.attack()
##        #check player health and if you die, play death animation
##        p.current_health -= enemyDamage    
    #if the player is still alive, reset the gameplay loop
        
    pygame.display.update()
pygame.quit()
