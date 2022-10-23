import copy
import sys, math, random
from skills import skills_initial

default_attributes ={
    "Strength": 50,
    "Constitution": 50,
    "Size": 50,
    "Dexterity": 50,
    "Appearance": 50,
    "Education": 50,
    "Intelligence": 50,
    "Willpower": 50,
    "Luck": 10,
}
default_current_condition ={
# values are current / max
    "Sanity": [10, 10],
    "Hit Points": [1, 1],
    "Magic Points": [1, 1],
    "Status": ["OK"],
# conditions od Wounds is [1:0] is Major Wound, and [*,1] is KO...
    "Wounds": ["OK"],
# conditions od Death is [1:0] is a dying state, and [*,1] means Dead...
    "Death": ["Alive"]
}
default_weapons ={
#   {Name}   [Instock][Damage][SkillForUse][SkillRequiments][MaxRange][EquipmentSlot][Nslots]
    "Short Sword":[1, "1D6+B", "Melee Weapon", 20, 3, "Weapon", 1],
    "Unarmed": [1, "1D3+B", "Fist/Punch", 5, 1, "Weapon", 2]
}
default_armor={
# armors are [True]in items[True]equiped[]force against physical[]bonus magical[]dura[]equpment slot
    "Clothes":[True, True, 1, 1, 20, "body"]
}
default_items={
# items are []count by num, []effect
    "Small Healing Potion":[1, "Heal Small"]
}
default_equipment={
    "Weapon": [None, None],
    "Armor": [None],
    "Acessory": [None, None]
}

class Creature:
    def __init__(self, name: str, race: str):
        self.creature = [name, race]
        self.condition = (copy.deepcopy(default_current_condition))
        self.attributes = (copy.deepcopy(default_attributes))
        self.skills = (copy.deepcopy(skills_initial))
        self.weapon = copy.deepcopy(default_weapons)
        self.armor = copy.deepcopy(default_armor)
        self.items = copy.deepcopy(default_items)
        self.equipment = copy.deepcopy(default_equipment)
    def __str__(self):
        return str(self)

    def find_skill_value(self, skill_name):
        #print(f'{self.creature[0]} skill {skill_name} is: {self.skills[skill_name][0]}')
        return self.skills[skill_name][0]

    def raise_skill(self, skill_name):
        result_of_dice = self.dice(100)
        current = self.find_skill_value(skill_name)
        if result_of_dice > current:
            if result_of_dice >= current + 10:
                current += 10
            else:
                current = result_of_dice
            print(f"Congratulation's {self.creature[0]} skill of {skill_name} rises to {current}")
            self.skills[skill_name][0] = current
    def inspect_skills(self):
        print(f"\n============================== Let's look skills of {self.creature[0]} ==============================", end="")
        new_list = []
        for key in self.skills:
            new_list.append(f'{key}:{self.skills[key][0]}')

        x = 0
        for i in new_list:
            if x % 6 == 0:
                print()
            print(i, end=' | ')
            x += 1
        print(f"\n============================ That's the end of {self.creature[0]} skills list ============================\n")
    def dice(self, num):
        if num in (4, 6, 8, 20):
            result = random.randrange(1, num)
            print(f"Result of {num} sided knuckle dice is {result}")
            return result
        elif num == 100:
            first_dice = random.randrange(0, 9)
            second_dice = random.randrange(0, 9)
            print(f"The ten's dice is {first_dice} and unit dice is {second_dice}")
            result = int(str(first_dice) + str(second_dice))
            if result == 0:
                result = 100
            print(result)
            return result

    def dice_success_attributes(self, cond):
        num = self.dice(100)
        chosen_cond = self.choose_attribute(cond)
        if num <= chosen_cond / 5:
            print("Extreme success")
            return "Extreme success"
        elif num <= chosen_cond / 2:
            print("Hard success")
            return "Hard success"
        elif num <= chosen_cond:
            print("Regular success")
            return "Regular success"
        else:
            print("Failed")
            return "Failed"

    def take_damage(self, value):
        hp_init = self.condition["Hit Points"][0]
        hp_max = self.condition["Hit Points"][1]
        if hp_max <= value:
            hp_new = 0
            self.condition["Death"] = ["DEAD"]
        elif hp_max / 2 <= value:
            hp_new = hp_init - value
            print(f'{self.creature[0]} is getting hit with major damage\n'
                  f'now its time to check for CON attribute:{self.choose_attribute("Constitution")}')
            if self.dice_success_attributes("Constitution") == "Failed":
                self.condition["Wounds"] = ["Major Wound"]
                print(f"{self.creature[0]} get wounded with major damage: {value}")
        else:
            hp_new = hp_init - value
            print(f"{self.creature[0]} get minor damage: {value}")

        if self.condition["Death"] == ["Dying"]:
            if self.dice_success_attributes("Constitution") == "Failed":
                self.condition["Death"] = ['DEAD']

        elif hp_new <= 0 and self.condition["Death"] != ["DEAD"]:
            hp_new = 0
            self.condition["Death"] = ["Dying"]
            print(f"{self.creature[0]} HP has fall to Zero, now {self.creature[0]} is at the dying state")
            if self.dice_success_attributes("Constitution") == "Failed":
                self.condition["Death"] = ["DEAD"]
                print(f"{self.creature[0]} FAILED to survive, now he is DEAD")
            else:
                print(f"{self.creature[0]} SUCCEED to survive, but he is at dying state")

        self.condition["Hit Points"][0] = hp_new
        print(f'{self.creature[0]} left {self.condition["Hit Points"][0]} of {self.condition["Hit Points"][1]} HP')

    def check_current_condition(self):
        print(f"\n======================= Let's look at conditions of {self.creature[0]} =======================")
        for cond in self.condition:
            print(f'{self.creature[0]} got {cond} status {self.condition[cond]}')
        print(f"========================== That's the end of {self.creature[0]} condition list ===========================\n")
    def choose_attribute(self, stat):
        return self.attributes[stat]

    def choose_current_condition(self, condition):
        return self.condition[condition][1]

    def choose_max_condition(self, condition):
        return self.condition[condition][0]



    def inspect_weapons(self):
        print(f"\n============================ Let's look what weapon's do {self.creature[0]} have ============================")
        for weapon in self.weapon:
            if self.weapon[weapon][0] > 0 and self.equipment["Weapon"][0] == weapon:
                print(f'EQUIPPED with {weapon}: '
                      f'|| QTY:{self.weapon[weapon][0]} || DMG:{self.weapon[weapon][1]} || SKL: {self.weapon[weapon][2]}:{self.weapon[weapon][3]}'
                      f' || RNG:{self.weapon[weapon][4]} || Hands to equip:{self.weapon[weapon][6]}')
            elif self.weapon[weapon][0] > 0:
                print(f'{weapon}: '
                      f'|| QTY:{self.weapon[weapon][0]} || DMG:{self.weapon[weapon][1]} || SKL: {self.weapon[weapon][2]}:{self.weapon[weapon][3]}'
                      f' || RNG:{self.weapon[weapon][4]} || Hands to equip:{self.weapon[weapon][6]}')
        print(f"============================= That's the end of {self.creature[0]} weapons list =============================\n")
    def equip_weapon(self, weapon):
        if self.equipment["Weapon"][0] == weapon:
            print(f'Listen to me {self.creature[0]}, you all ready equipped with {weapon}')
        elif self.weapon[weapon][0] == 0:
            print(f'Listen to me {self.creature[0]}, for successfully equip some {weapon}, you need to buy at least one {weapon}')
        else:
            if self.weapon[weapon][6] == 1:
                if self.weapon[weapon][0] >= 1 and self.equipment["Weapon"][0] != weapon:
                    if self.equipment["Weapon"][0] != self.equipment["Weapon"][1]:
                        if self.equipment["Weapon"][0] == None:
                            self.equipment["Weapon"][0] = weapon
                            print(f'{weapon} was successfully equipped by {self.creature[0]}')
                        else:
                            print(f'{self.equipment["Weapon"][0]} was unequipped by {self.creature[0]}')
                            print(f'{weapon} was successfully equipped by {self.creature[0]}')
                    else:
                        if self.equipment["Weapon"][1] != None:
                            print(f'{self.equipment["Weapon"][1]} was unequipped by {self.creature[0]}')
                        self.equipment["Weapon"][0] = weapon
                        self.equipment["Weapon"][1] = None
                        print(f'{weapon} was successfully equipped by {self.creature[0]}')
            elif self.weapon[weapon][6] == 2:
                self.equipment["Weapon"][0] = weapon
                self.equipment["Weapon"][1] = weapon
                print(f'{weapon} was successfully equipped by {self.creature[0]}')

    def inspect_equipment(self):
        print(f"\n============================== Let's look what is putted on {self.creature[0]} ==============================")
        for key in self.equipment:
            print(f'{key} {self.equipment[key]}')
        print(f"============================ That's the end of {self.creature[0]} equipment list ============================\n")
    def choose_item(self, item):
        self.item = item

    def choose_spell(self, spell):
        self.spell = spell


'''

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

'''


player_1 = Creature("Alex", "human")
player_2 = Creature("Den", "elf")
player_1.equip_weapon("Short Sword")
player_1.condition["Hit Points"] = [12, 12]
player_1.condition["Magic Points"] = [10, 10]
'''
player_2.equip_weapon("Short Sword")
player_1.equip_weapon("Unarmed")
player_1.inspect_weapons()
player_2.inspect_weapons()
player_2.inspect_equipment()
player_1.inspect_equipment()
player_2.equip_weapon("Short Sword")
'''
#player_1.raise_skill("Accounting")
#player_1.skills["Melee Weapon"][0] = 40
#player_2.raise_skill("Melee Weapon")
#player_1.inspect_skills()
#player_1.check_current_condition()
player_1.take_damage(11)
player_1.take_damage(3)
player_1.check_current_condition()
