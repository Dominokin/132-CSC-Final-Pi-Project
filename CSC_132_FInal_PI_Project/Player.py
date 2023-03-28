class Player:
    def __init__(self, max_health = 30, current_health = 30, damage, level):
        self.max_health = max_health
        self.current_health = current_health
        self.damage = damage
        self.level = level
        self.potions = potions

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
    def current_health(self, value):
        if(self._current_health > self._max_health):
            self._current_health = self._max_health
        else:
            self._current_health = value

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

    def heal(self, value):
        if(potions > 0):
            self.current_health += 20
        else:
            print("You have no more health potions")

        
