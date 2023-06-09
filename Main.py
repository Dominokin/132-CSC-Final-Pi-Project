import RPi.GPIO as GPIO
import math
from random import randint
import pygame
from time import *
from pygame.locals import MOUSEBUTTONDOWN

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
        self.xp = 0
        self.xp_lvl_up = 10
        self.animation_list = []
        self.frame = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()
        self.animation_cooldown = 80
        #Background removal color
        BG_REMOVE = (113, 102, 79)
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
                temp_image = self.get_img(img, x, 96, 64, 4, BG_REMOVE)
                temp_list.append(temp_image)
            self.animation_list.append(temp_list)
            #Next is the attack frames
            temp_list = []
            img = pygame.image.load(f"AllCharacters/{self.name}/{self.name}Attack_strip.png")
            for x in range(self.animation_steps[f"{self.name}Attack"]):
                temp_image = self.get_img(img, x, 144, 64, 4, BG_REMOVE)
                temp_list.append(temp_image)
            self.animation_list.append(temp_list)
            #last is the death frames
            temp_list = []
            img = pygame.image.load(f"AllCharacters/{self.name}/{self.name}Death_strip.png")
            for x in range(self.animation_steps[f"{self.name}Death"]):
                temp_image = self.get_img(img, x, 96, 64, 4, BG_REMOVE)
                temp_list.append(temp_image)
            self.animation_list.append(temp_list)
        else:
            for x in range(self.animation_steps[f"{self.name}Idle"]):
                temp_image = self.get_img(img, x, 64, 64, 4, BG_REMOVE)
                temp_list.append(temp_image)
            self.animation_list.append(temp_list)
            #Next is the attack frames
            temp_list = []
            img = pygame.image.load(f"AllCharacters/{self.name}/{self.name}Attack_strip.png")
            for x in range(self.animation_steps[f"{self.name}Attack"]):
                temp_image = self.get_img(img, x, 64, 64, 4, BG_REMOVE)
                temp_list.append(temp_image)
            self.animation_list.append(temp_list)
            #last is the death frames
            temp_list = []
            img = pygame.image.load(f"AllCharacters/{self.name}/{self.name}Death_strip.png")
            for x in range(self.animation_steps[f"{self.name}Death"]):
                temp_image = self.get_img(img, x, 64, 64, 4, BG_REMOVE)
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

    @y.setter
    def y(self, value):
        self._y = value

    @property
    def xp(self):
        return self._xp

    @xp.setter
    def xp(self, value):
        self._xp = value

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
        if(newHealth <= 0):
            self._current_health = 0
        else:
            self._current_health = round(newHealth)

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
        if self.name == "Knight":
            screen.blit(self.image, self.rect)
        else:
            self.image = pygame.transform.flip(self.image, True, False)
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
                if self.action == 2:
                    self.frame = len(self.animation_list[self.action]) - 1
                else:
                    self.idle()

    def idle(self):
        self.action = 0
        self.frame = 0
        self.update_time = pygame.time.get_ticks()

    def death(self):
        self.action = 2
        self.frame = 0
        self.update_time = pygame.time.get_ticks()
        
    def heal(self):
        if(self.potions > 0):
            temp_health = self.current_health + 20
            if temp_health >= self.max_health:
                self.current_health = self.max_health
            else:
                self.current_health += 20
        else:
            return "You have no more health potions"

    def attack(self):
        #take away health, with the amount of health taken away by the-
        #attack damage integer
        rand_num = round(self.damage * 0.75)
        choose_dam = randint(rand_num, self.damage)
        attack_damage = choose_dam
        crit = randint(0,51)
        #if crit hit, then make damage increase
        if crit >= 25:
            attack_damage *= 1.3
        #set variable to attack animation
        self.action = 1
        self.frame = 0
        self.update_time = pygame.time.get_ticks()
        return attack_damage

    def level(self):
        pass

    #scale health and damage. Can be adjusted later
    def scale(self):
        global enc_num
        if enc_num % 3 == 0:
            scale_amount = ((enc_num/3)*1.1)
            self.max_health = round(scale_amount * self.max_health)
            self.damage = round(scale_amount * self.damage)

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
        temp_image = pygame.Surface((width, height)).convert()
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

#use broadcom pin mode
GPIO.setmode(GPIO.BCM)

#setup the pins for attacking, healing, or fleeing
attack = 19
heal = 21
flee = 13

#setup the input pins
GPIO.setup(attack, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(heal, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(flee, GPIO.IN, GPIO.PUD_DOWN)

#set the area for the bottom pannel to display character's stuff
bottom_pannel = 150
#define screen dimentions
screen_width = 785
screen_height = 442 + bottom_pannel

#game variables
current_turn = 1
total_turns = 2
#action cooldown for the ai enemies
action_cooldown = 0
action_wait_time = 90
RED = (178, 8, 8)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#font for the endgame screen
font = pygame.font.Font(None, 30)

#set up the font for the text
font_2 = pygame.font.SysFont("Arial", 20)

#set the text for the death screen
restart = font.render("RESTART", True, WHITE, RED)
leave = font.render("EXIT", True, WHITE, RED)

#set the rect object for the end screen text
textRect_restart = restart.get_rect(center=(screen_width/2.3, screen_height/2))
textRect_leave = leave.get_rect(center=(screen_width/1.7, screen_height/2))

#set the frame rate for animations
clock = pygame.time.Clock()
fps = 30

#set up the display
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Final Pi Project game thing idk")

#load images and use functions for drawing them onto the screen
background_img = pygame.image.load('Background/dungeon-bg.jpeg').convert_alpha()
def draw_bg():
    screen.blit(background_img, (0,0))

def draw_hud():
    pygame.draw.rect(screen, BLACK, (10, screen_height - bottom_pannel + 60, 150, 20))
    #draw the player's health bar
    player_hp_ratio = p.current_health/p.max_health
    pygame.draw.rect(screen, BLACK, (10, screen_height - bottom_pannel + 10, 150, 20))
    pygame.draw.rect(screen, RED, (10, screen_height - bottom_pannel + 35, 150\
                                   , 20))
    pygame.draw.rect(screen, GREEN, (10, screen_height - bottom_pannel + 35, \
                                     150*player_hp_ratio, 20))

    #draw the player's potion count
    potion_img = pygame.image.load("Icons/icons/32x32/potion_01a.png").convert_alpha()
    spacing = 0
    pygame.draw.rect(screen, BLACK, (spacing, screen_height - bottom_pannel + 85, 150, 40))
    for i in range(p.potions):
        screen.blit(potion_img, (spacing, screen_height - bottom_pannel + 85))
        spacing += 25

    #draw the enemy's health bar
    enemy_hp_ratio = newEnemy.current_health/newEnemy.max_health
    pygame.draw.rect(screen, BLACK, (screen_width/2 + 10, screen_height - bottom_pannel + 10, 150, 20))
    pygame.draw.rect(screen, RED, (screen_width/2 + 10, screen_height - bottom_pannel\
                                   +35, 150, 20))
    pygame.draw.rect(screen, GREEN, (screen_width/2 + 10, screen_height - bottom_pannel\
                                     + 35, 150*enemy_hp_ratio, 20))
        
#instantiate the player
p = Game(250, 350, "Knight", 30, 30, 10, 1, 1)

#make enemy types
#this will also load sprite sheets into its respective self.animation_list
bat = Game(550, 325, "Bat", 10, 10, 5, 1, 0)
witch = Game(550, 325, "Witch", 20, 20, 10, 1, 0)
wolf = Game(550, 325, "Wolf", 15, 15, 8, 1, 0)

#put all instatntiated characters in a dict
#makes random enemies easier
#allows all sprite sheets to be loaded in for animation
sprite_dict = {0: bat, 1: witch, 2: wolf, 3:p}

#instantiate the enemy
newEnemy = None

#keep track of the encounter number
enc_num = 1

#set the game over variable to false
game_over = False

######################## THIS IS THE MAIN GAME LOOP #######################
running = True
while(running):
    #checking for exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == MOUSEBUTTONDOWN:
            #get mouse position
            mpos = pygame.mouse.get_pos()
            if pygame.mouse.get_pressed():
                if textRect_restart.collidepoint(mpos):
                    p.current_health = 30
                    p.max_health = 30
                    p.damage = 10
                    p.level = 1
                    p.xp = 0
                    p.potions = 1
                    bat.current_health = 10
                    bat.max_health = 10
                    bat.damage = 5
                    witch.current_health = 20
                    witch.max_health = 20
                    witch.damage = 10
                    wolf.current_health = 15
                    wolf.max_health = 15
                    wolf.damage = 8
                    enc_num = 1
                    p.idle()
                    game_over = False
                elif textRect_leave.collidepoint(mpos):
                    running = False
    #set frame rate
    clock.tick(fps)

    #draw the background
    draw_bg()

    #spawn random enemy type
    if newEnemy == None:
        choose_enemy = randint(0, 2)
        newEnemy = sprite_dict[choose_enemy]
        newEnemy.current_health = newEnemy.max_health
        newEnemy.idle()
        print(f"Enemy Health: {newEnemy.current_health}")
        print(f"Enemy Damage: {newEnemy.damage}")
    p.update()
    p.draw()
    newEnemy.update()
    newEnemy.draw()

    #draw the hud
    draw_hud()
    level_hud = font_2.render(f"Level: {p.level}", True, WHITE, None)
    player_hud = font_2.render(f"HP: {p.current_health}/{p.max_health}", True, WHITE, None)
    enemy_hud = font_2.render(f"HP: {newEnemy.current_health}/{newEnemy.max_health}", True, \
                 WHITE, None)
    screen.blit(player_hud, (10, screen_height - bottom_pannel + 10))
    screen.blit(enemy_hud, (screen_width/2 + 10, screen_height - bottom_pannel \
                            + 10))
    screen.blit(level_hud, (10, screen_height - bottom_pannel + 60))

        #let player go first
    if p.current_health > 0:
        #if it is the player's turn
        if current_turn == 1:
            #check for inputs
            #if the player attacks, use the player.attack method in the Player class
            if GPIO.input(attack):
                damage = p.attack()
                newEnemy.current_health -= damage
                if newEnemy.current_health <= 0:
                    newEnemy.death()
                    enc_num += 1
                    p.xp += randint(10, 30)
                    potion_chance = randint(0, 30)
                    for enemy in range(len(sprite_dict) - 1):
                        sprite_dict[enemy].scale()
                    if potion_chance > 20:
                        p.potions += 1
                action_cooldown = 0
                current_turn += 1
            #if the players heals, use the player.heal method in the Player class
            elif GPIO.input(heal):
                p.heal()
                print(p.current_health)
                p.potions -= 1
                action_cooldown = 0
                current_turn += 1
            #if the player flees, pass all of this and restart the encounter
            elif GPIO.input(flee):
                newEnemy = None
                action_cooldown = 0
                current_turn += 2
                    
        #if player doesn't flee, use the enemy attack method in the enemy class
        if current_turn == 2:
            action_cooldown += 1
            if action_cooldown >= action_wait_time:
                if newEnemy.current_health > 0:
                    enemyDamage = newEnemy.attack()
                    #check player health and if you die, play death animation
                    p.current_health -= enemyDamage
                    print(p.current_health)
                    if p.current_health <= 0:
                        p.death()
                    current_turn += 1
                    action_cooldown = 0
                else:
                    current_turn = 1
                    newEnemy = None
                    
        #if the player is still alive, reset the gameplay loop
        if current_turn > total_turns:
                    current_turn = 1

    #if the player falls below 0 health, end the game
    else:
        game_over = True

    #player leveling up
    if p.xp > p.xp_lvl_up:
        p.level += 1
        p.xp -= p.xp_lvl_up
        p.xp_lvl_up = round(p.xp_lvl_up * 1.15)
        p.damage += 5
        p.max_health += 5
        print(f"XP: {p.xp}")
            

    if game_over:
        #set the game over screen rectangle and put in the encounter num
        #along with exit and restart buttons
        gameover_text = font.render(f"Game Over! You defeated {enc_num - 1} enemies",\
                                   True, WHITE, RED)
        textRect_gameover = gameover_text.get_rect(center=(screen_width/2,\
                                                          screen_height/2.3))
        screen.blit(gameover_text, textRect_gameover)
        screen.blit(restart, textRect_restart)
        screen.blit(leave, textRect_leave)
    pygame.display.update()
pygame.quit()
