import pygame
from random import randint

class Enemy:
    def __init__(self, x, y, name, health, damage):
        self.x = x
        self.y = y
        self.name = name
        self.health = health
        self.damage = damage
        self.alive = True
        img = pygame.image.load(f'AllCharacters/{self.name}/{self.name}Idle_strip.png')
        self.image = pygame.transform.scale(img, (img.get_width() * 2, img.get_height() * 2))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def draw(self):
        screen.blit(self.image, self.rect)
        
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x= value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y= value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, newHealth):
        if newHealth <= 0:
            self._health = 0
        else:
            self._health = newHealth

    @property
    def damage(self):
        return self._damage

    @damage.setter
    def damage(self, value):
        self._damage= value

    def attack(self):
        crit = randint(0, 51)
        damage = randint(0, self.damage+1)
        if crit >= 25:
            damage *= 1.5
        return damage
