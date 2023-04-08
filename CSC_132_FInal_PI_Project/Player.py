import pygame
class Player:
    def __init__(self, x, y, current_health, max_health, damage, level):
        self.x = x
        self.y = y
        self.current_health = current_health
        self.max_health = max_health
        self.damage = damage
        self.level = level
        self.potions = 1
        self.action = 'KnightIdle_strip'
        img = pygame.image.load(f'AllCharacters/Knight/{self.action}.png')
        self.image = pygame.transform.scale(img, (img.get_width() * 2, img.get_height() * 2))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

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
    

    def heal(self, value):
        if(potions > 0):
            self._current_health += 20
        else:
            return "You have no more health potions"

    def attack(self):
        attack_damage = randint(1, self.damage)
        self.action = 'KnightAttack_strip'
        #takes away health, with the amount of health taken away by the
        #attack damage integer
        pass

    def flee(self):
        #resets the encounter, with a new enemy, keeping same health and items, coins
        pass
