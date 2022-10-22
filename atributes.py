import sys, math
from dice import dice

class Creature:
    def __init__(self, atributes=None, weapon=None, armor=None, item=None, spell=None):
        self.atributes = atributes
        self.weapon = weapon
        self.armor = armor
        self.item = item
        self.spell = spell

    def __str__(self):
        result = str(self)
        print(f"{result}")

class Atributes(Creature):
    def __init__(self, str: int, con: int, siz: int, dex: int, app: int, edu: int, int: int, pow: int,
                 hp: int, mp: int, luck: int, san: int, race: str):
        self.str = str
        self.con = con
        self.siz = siz
        self.dex = dex
        self.app = app
        self.edu = edu
        self.int = int
        self.pow = pow
        self.hp = hp
        self.mp = mp
        self.luck = luck
        self.san = san
        self.race = race
        super().__init__(atributes=self)

    def __str__(self):
        result = str(self)
        print(f"{result}")

    def choose_stat(self, stat):
        if stat == "str":
            return self.str
        elif stat == "con":
            return self.con
        elif stat == "dex":
            return self.dex
        elif stat == "int":
            return self.int
        elif stat == "siz":
            return self.siz
        elif stat == "app":
            return self.app
        elif stat == "luck":
            return self.luck
        elif stat == "hp":
            return self.hp
        elif stat == "mp":
            return self.mp
        elif stat == "pow":
            return self.pow
        elif stat == "san":
            return self.san
        elif stat == "edu":
            return self.edu
        elif stat == "race":
            return self.race
        else:
            sys.exit("bug in choose_stat")

    def choose_weapon(self, weapon):
        self.weapon = weapon

    def choose_item(self, item):
        self.item = item

    def choose_spell(self, spell):
        self.spell = spell

    def upgrade_stat(self, stat, value):
        if stat in ("san", "hp", "mp", "luck"):
            if stat == "san":
                self.san += value
            elif stat == "hp":
                self.hp += value
            elif stat == "mp":
                self.mp += value
            else:
                self.luck += value
        else:
            print("can't modify that value")


class Weapons(Creature):
    def __init__(self, name: str, damage: str, range, type, hand):
        self.name = name
        self.damage = damage
        self.range = range
        self.type = type
        self.hand = hand
        super().__init__(weapon=self)

    def dealt_damage(self, range):
        damage = self.damage
        if self.type in ("bow", "rifle", "throw axes", "gun"):
            type = "ranged"
        else:
            type = "mele"
        if damage[0] == "1":
            damage_value = dice(int(damage[2]))
        elif damage[0] == "2":
            damage_value = dice(int(damage[2]))+dice(int(damage[2]))
        elif damage[0] == "3":
            damage_value = dice(int(damage[2])) + dice(int(damage[2])) + dice(int(damage[2]))
        else:
            pass
        if damage[-2] == "+":
            damage_value += int(damage[-1])
        else:
            pass
        if range > self.range:
            if type == "mele":
                print("mele weapon is useles on that distance")
                damage_value = 0
            elif range > (self.range * 2):
                print("target is too far away")
                damage_value = 0
            else:
                print("better to get closer to inflict more damage")
                damage_value = math.floor(damage_value/2)
        elif range < self.range/3 and type == "ranged":
            print("better to increase the distance to inflict more damage")
            damage_value = math.floor(damage_value/1.5)
        else:
            pass
        return (damage_value)


    def __str__(self):
        result = f"{str(self.weapon.name)}\n" \
                 f"Damage: {str(self.weapon.damage)}\n" \
                 f"Range: {str(self.weapon.range)}\n" \
                 f"Class: {str(self.weapon.type)}\n" \
                 f"Type: {str(self.weapon.hand)}"
        print(f"{result}")