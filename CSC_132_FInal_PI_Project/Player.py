import pygame
class Player:
    def __init__(self, x, y, name, current_health, max_health, damage, level):
        self.x = x
        self.y = y
        self.name = name
        self.current_health = current_health
        self.max_health = max_health
        self.damage = damage
        self.level = level
        self.potions = 1
        self.animation_list = []
        self.frame = 0
        self.action = 0
        update_time = pygame.time.get_ticks()
        #load the sprite sheets
        self.animation_list.append("AllCharacters/Knight/KnightIdle_strip.png")
        self.animation_list.append("AllCharacters/Knight/KnightAttack_strip.png")
        self.animation_list.append("AllCharacters/Knight/KnightDeath_strip.png")
        self.image = pygame.image.load(self.animation_list[self.action])
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
            self._action = 'KnightDeath_strip'
            #maybe have a screen pop up saying YOU DIED or something like that
            pass
        else:
            self._current_health = newHealth

    @property
    def damage(self):
        return self._damage

    @damage.setter
    def damage(self, value):
        self._damage = value + 1

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

    def update(self):
        last_update = pygame.time.get_ticks()
        #update animation
        current_time = pygame.time.get_ticks()
        #if the time that has past since the last update is longer than the animation cooldown...
        if current_time - last_update >= animation_cooldown:
            #update the frame and reset the recent update to the last tick
            self.frames += 1
            last_update = current_time
            if self.frames >= animation_steps:
                self.frames = 0
            
        #show the animation on the screen
        screen.blit(animation_list[frame], (0,0))

    def heal(self, value):
        if(potions > 0):
            self._current_health += 20
        else:
            return "You have no more health potions"

    def attack(self):
        attack_damage = randint(1, self.damage)
        self.frames = 22
        self.action = 'KnightAttack_strip'
        crit = randint(0,51)
        if crit >= 25:
            attack_damage *= 1.3
        #takes away health, with the amount of health taken away by the-
        #attack damage integer
        return attack_damage

    def flee(self):
        #resets the encounter, with a new enemy, keeping same health and items, coins
        pass
