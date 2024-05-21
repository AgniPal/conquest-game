from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def attack(self):
        print("Боец выбирает меч. Рубит мечём")

class Bow(Weapon):
    def attack(self):
        print("Боец выбирает лук. Стреляет горящими стрелами")

class Figher():
    def __init__(self):
        self.weapon = None

    def choice_Weapon(self, weapon):
        self.weapon = weapon
        self.weapon.attack()


class Monster():
    def fight(self):
        print("Монстр атакует")

    def dead(self):
        print("Монстр убит")


sword = Sword()
bow = Bow()

figher = Figher()
monster = Monster()

monster.fight()
figher.choice_Weapon(sword)

monster.fight()
figher.choice_Weapon(bow)
monster.dead()