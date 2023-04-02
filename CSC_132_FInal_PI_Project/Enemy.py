class Enemies:
    def __init__(self, health, damage):
        self.health = health
        self.damage = damage

    @property
    def health(self):
        return self._heath

    @health.setter
    def health(self, value):
        self._health= value

    @property
    def damage(self):
        return self._damage

    @health.setter
    def damage(self, value):
        self._damage= value
