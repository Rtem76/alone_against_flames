import copy
import random
from skills import skills_initial

default_attributes = {
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
default_current_condition = {
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
default_weapons = {
    #   {Name}   [Qtty][Damage][SkillForUse][SkillRequiments][MaxRange][EquipmentSlot][Nslots]
    # format of Damage => [xDy] 'x'-time Dice 'y'-num  [+S](Str bonus == low Str - 40 / 20) [+D] (dex bonus-same as str)
    "Short Sword": [1, "1D6", "Melee Weapon", 20, 3, "Weapon", 1],
    "Unarmed": [1, "2D3+2", "Fist/Punch", 5, 1, "Weapon", 2],
    "Iron Knuckles": [0, "2D6+2", "Fist/Punch", 40, 3, "Weapon", 2],
    "Pistol": [1, "2D3+1+1D4", "Handgun", 20, 30, "Weapon", 1]
}
default_armor = {
    # armors are [True]in items[True]equiped[]force against physical[]bonus magical[]dura[]equpment slot
    "Clothes": [True, True, 1, 1, 20, "body"]
}
default_items = {
    # items are []count by num, []effect
    "Small Healing Potion": [1, "Heal Small"]
}
default_equipment = {
    "Weapon": [None, None],
    "Armor": [None],
    "Acessory": [None, None]
}


class Creature:
    def __init__(self, is_player: bool, name: str, race: str):
        self.up_extreme = True
        self.up_hard = False
        # Attacks Per Round.
        self.apr = 3
        self.default = "Fight back"
        self.is_player = is_player
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
        # print(f'{self.creature[0]} skill {skill_name} is: {self.skills[skill_name][0]}')
        return self.skills[skill_name][0]

    def raise_skill(self, skill_name):
        print(f'{self.creature[0]} has an attempt to raise the {skill_name} skill')
        result_of_dice = self.dice(100)
        current = self.find_skill_value(skill_name)
        if result_of_dice > current:
            if result_of_dice >= current + 10:
                current += 10
            else:
                current = result_of_dice
            print(f"Congratulation's {self.creature[0]} skill of {skill_name} upgraded to {current}")
            self.skills[skill_name][0] = current
        else:
            print(f'{self.creature[0]} Failed his attempt to upgrade his {skill_name} skill')
    def inspect_skills(self):
        print(
            f"\n============================== Let's look skills of {self.creature[0]} ==============================",
            end="")
        new_list = []
        for key in self.skills:
            new_list.append(f'{key}:{self.skills[key][0]}')

        x = 0
        for i in new_list:
            if x % 6 == 0:
                print()
            print(i, end=' | ')
            x += 1
        print(
            f"\n============================ That's the end of {self.creature[0]} skills list ============================\n")

    def dice(self, num):
        if num in (3, 4, 6, 8, 20):
            result = random.randrange(1, num)
            print(f"Result of {num} sided knuckle dice is {result}")
            return result
        elif num == 100:
            first_dice = random.randrange(0, 9)
            second_dice = random.randrange(0, 9)
            result = int(str(first_dice) + str(second_dice))
            if result == 0:
                result = 100
            print(f"The ten's dice is {first_dice} and unit dice is {second_dice} equal to {result}")
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

    def dice_success_skill(self, skill):
        num = self.dice(100)
        chosen_cond = self.choose_skill(skill)
        if num <= chosen_cond / 5:
            print("Extreme success")
            if self.up_extreme:
                self.raise_skill(skill)
            return "Extreme success"
        elif num <= chosen_cond / 2:
            print("Hard success")
            if self.up_hard:
                self.raise_skill(skill)
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
            if self.is_player == False:
                self.condition["Death"] = ["DEAD"]
            if hp_new < 0:
                hp_new = 0
            if self.dice_success_attributes("Constitution") == "Failed":
                self.condition["Death"] = ['DEAD']

        elif hp_new <= 0 and self.condition["Death"] != ["DEAD"]:
            hp_new = 0
            if self.is_player == True:
                self.condition["Death"] = ["Dying"]
                print(f"{self.creature[0]} HP has fall to Zero, now {self.creature[0]} is at the dying state")
                if self.dice_success_attributes("Constitution") == "Failed":
                    self.condition["Death"] = ["DEAD"]
                    print(f"{self.creature[0]} FAILED to survive, now he is DEAD")
                else:
                    print(f"{self.creature[0]} SUCCEED to survive, but he is at dying state")
            else:
                self.condition["Death"] = ["DEAD"]
        self.condition["Hit Points"][0] = hp_new
        print(f'{self.creature[0]} left {self.condition["Hit Points"][0]} of {self.condition["Hit Points"][1]} HP')

    def check_current_condition(self):
        print(f"\n======================= Let's look at conditions of {self.creature[0]} =======================")
        for cond in self.condition:
            print(f'{self.creature[0]} got {cond} status {self.condition[cond]}')
        print(
            f"========================== That's the end of {self.creature[0]} condition list ===========================\n")

    def choose_attribute(self, stat):
        return self.attributes[stat]

    def choose_skill(self, stat):
        return self.skills[stat][0]

    def choose_current_condition(self, condition):
        return self.condition[condition][1]

    def choose_max_condition(self, condition):
        return self.condition[condition][0]

    def lllllllllllllllllllllll(self):
        print("DEVELOPMENT in PROGRESS this option is under DEVELOPMENT")

    def run_inventory(self):
        while True:
            user_input = input("\n========== Inventory options: ========== \n"
                               "[1] for check [2] for change [3] for use [0] to exit\n"
                               "======================================== \n"
                               "INPUT: ")
            if user_input == "1":
                self.run_inventory_check()
            elif user_input == "2":
                self.lllllllllllllllllllllll()
            elif user_input == "3":
                self.lllllllllllllllllllllll()
            elif user_input == "0":
                break
            else:
                print("Wrong Input, only single digit [1,2,3,0] is acceptable")

    def run_inventory_check(self):
        while True:
            user_input = input("\n=============== Check inventory options: =============== \n"
                               "[1] equipped items [2] list of weapons [3] list of items\n"
                               "[4] list of armors [5] list of accessories [0] return\n"
                               "======================================================== \n"
                               "INPUT: ")
            if user_input == "1":
                self.inspect_equipment()
            elif user_input == "2":
                self.inspect_weapons()
            elif user_input == "3":
                self.lllllllllllllllllllllll()
            elif user_input == "4":
                self.lllllllllllllllllllllll()
            elif user_input == "5":
                self.lllllllllllllllllllllll()
            elif user_input == "0":
                break
            else:
                print("Wrong Input, only single digit [1,2,3,4,5,0] is acceptable")

    def inspect_weapons(self):
        print(
            f"\n============================ Let's look what weapon's do {self.creature[0]} have ============================")
        for weapon in self.weapon:
            if self.weapon[weapon][0] > 0 and self.equipment["Weapon"][0] == weapon:
                print(f'EQUIPPED with {weapon}: '
                      f'|| QTY:{self.weapon[weapon][0]} || DMG:{self.weapon[weapon][1]} || SKL: {self.weapon[weapon][2]}:{self.weapon[weapon][3]}'
                      f' || RNG:{self.weapon[weapon][4]} || Hands to equip:{self.weapon[weapon][6]}')
            elif self.weapon[weapon][0] > 0:
                print(f'{weapon}: '
                      f'|| QTY:{self.weapon[weapon][0]} || DMG:{self.weapon[weapon][1]} || SKL: {self.weapon[weapon][2]}:{self.weapon[weapon][3]}'
                      f' || RNG:{self.weapon[weapon][4]} || Hands to equip:{self.weapon[weapon][6]}')
        print(
            f"============================= That's the end of {self.creature[0]} weapons list =============================\n")

    def equip_weapon(self, weapon):
        if self.equipment["Weapon"][0] == weapon:
            print(f'Listen to me {self.creature[0]}, you all ready equipped with {weapon}')
        elif self.weapon[weapon][0] == 0:
            print(
                f'Listen to me {self.creature[0]}, for successfully equip some {weapon}, you need to buy at least one {weapon}')
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
        print(
            f"\n============================== Let's look what is putted on {self.creature[0]} ==============================")
        for key in self.equipment:
            print(f'{key} {self.equipment[key]}')
        print(
            f"============================ That's the end of {self.creature[0]} equipment list ============================\n")

    def choose_item(self, item):
        self.item = item

    def choose_spell(self, spell):
        self.spell = spell

    def choose_action_explore(self):
        while True:
            user_input = input(f"\n============= {self.creature[0]} it's your time for act: ============= \n"
                               f"[1] to run inventory [2] look at the map [3] action's\n"
                               " [4]  [5]  [0] pass\n"
                               "======================================================== \n"
                               "INPUT: ")
            if user_input == "1":
                self.run_inventory_check()
            elif user_input == "2":
                self.lllllllllllllllllllllll()
            elif user_input == "3":
                self.lllllllllllllllllllllll()
            elif user_input == "4":
                self.lllllllllllllllllllllll()
            elif user_input == "5":
                self.lllllllllllllllllllllll()
            elif user_input == "0":
                break
            else:
                print("Wrong Input, only single digit [1,2,3,4,5,0] is acceptable")

    def combat_seq(self,monster):
        if self.choose_attribute("Dexterity") >= monster.choose_attribute("Dexterity"):
            return "1"
        else:
            return "2"

    def success_to_num(self, success):
        result=0
        for item in ["Failed", "Regular success", "Hard success", "Extreme success"]:
            if item == success:
                return result
            result +=1


    def choose_action_attack(self):
        if self.is_player:
            while True:
                user_input = input(f"========== {self.creature[0]}"
                                   f" now it's your time to perform an attack:\n ========== "
                                   f"[1] perform an attack with the current weapon [2] use skill [3] use spell\n"
                                   " [4] use potion [5] other [0] pass\n"
                                   "======================================================= \n"
                                   "INPUT: ")
                if user_input == "1":
                    return self.check_attack_success()

                elif user_input == "2":
                    self.lllllllllllllllllllllll()
                elif user_input == "3":
                    self.lllllllllllllllllllllll()
                elif user_input == "4":
                    self.lllllllllllllllllllllll()
                elif user_input == "5":
                    self.lllllllllllllllllllllll()
                elif user_input == "0":
                    break
                else:
                    print("Wrong Input, only single digit [1,2,3,4,5,0] is acceptable")
        else:
            return self.check_attack_success()
    def choose_action_defend(self):
        if self.is_player:
            while True:
                user_input = input(
                    f"========== {self.creature[0]} now it's your time to defend: ========== \n"
                    f"[1] fight back [2] dodge [3] run away"
                    " [4] use potion [5] find cover [0] pass\n"
                    "======================================================== \n"
                    "INPUT: ")
                if user_input == "1":
                    return [self.check_fight_back_success(), "F"]

                elif user_input == "2":
                    self.lllllllllllllllllllllll()
                elif user_input == "3":
                    self.lllllllllllllllllllllll()
                elif user_input == "4":
                    self.lllllllllllllllllllllll()
                elif user_input == "5":
                    self.lllllllllllllllllllllll()
                elif user_input == "0":
                    break
                else:
                    print("Wrong Input, only single digit [1,2,3,4,5,0] is acceptable")
        else:
            if self.default == "Fight back":
                return [self.check_fight_back_success(), "F"]
            if self.default == "Dodge":
                return [self.check_dodge_success(), "D"]

    def check_weapon_attack(self, name):
        return (f'{self.weapon[name][1]}')

    def check_weapon_type(self, name):
        return (f'{self.weapon[name][2]}')

    def check_attack_success(self):
        print(f'{self.creature[0]} is preparing [{self.check_weapon_type(self.equipment["Weapon"][0])}]'
              f':[{self.find_skill_value(self.check_weapon_type(self.equipment["Weapon"][0]))}]'
              f' attack with [{self.equipment["Weapon"][0]}]')
        return (self.dice_success_skill(self.check_weapon_type(self.equipment["Weapon"][0])))

    def check_fight_back_success(self):
        print(f'{self.creature[0]} is preparing [{self.check_weapon_type(self.equipment["Weapon"][0])}]'
              f':[{self.find_skill_value(self.check_weapon_type(self.equipment["Weapon"][0]))}]'
              f' fight back with [{self.equipment["Weapon"][0]}]')
        return (self.dice_success_skill(self.check_weapon_type(self.equipment["Weapon"][0])))

    def check_dodge_success(self):
        print(f'{self.creature[0]} is preparing [{self.check_weapon_type(self.equipment["Weapon"][0])}]'
              f':[{self.find_skill_value(self.check_weapon_type(self.equipment["Weapon"][0]))}]'
              f' fight back with [{self.equipment["Weapon"][0]}]')
        return (self.dice_success_skill(self.check_weapon_type(self.equipment["Weapon"][0])))

    def attack_value(self):
        damage_form = self.check_weapon_attack(self.equipment["Weapon"][0])
        print(f'{self.creature[0]} is preparing [{self.check_weapon_type(self.equipment["Weapon"][0])}] attack with '
              f'[{self.equipment["Weapon"][0]}], which damage formula is [{damage_form}]')
        damage_inflict = 0
        if len(damage_form) == 3:
            for _ in range(int(damage_form[0])):
                damage_inflict += self.dice(int(damage_form[2]))
        elif len(damage_form) == 5:
            for _ in range(int(damage_form[0])):
                damage_inflict += self.dice(int(damage_form[2]))
            damage_inflict += int(damage_form[4])
        elif len(damage_form) == 7:
            for _ in range(int(damage_form[0])):
                damage_inflict += self.dice(int(damage_form[2]))
            for _ in range(int(damage_form[4])):
                damage_inflict += self.dice(int(damage_form[6]))
        elif len(damage_form) == 9:
            for _ in range(int(damage_form[0])):
                damage_inflict += self.dice(int(damage_form[2]))
            damage_inflict += int(damage_form[4])
            for _ in range(int(damage_form[6])):
                damage_inflict += self.dice(int(damage_form[8]))
        return damage_inflict


'''

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


def main():
    monster_1 = Creature(False, "Murche Barca Keen", "goblin")
    player_1 = Creature(True, "Alex", "human")
    player_2 = Creature(True, "Den", "elf")
    player_1.equip_weapon("Short Sword")
    player_1.condition["Hit Points"] = [12, 12]
    player_1.condition["Magic Points"] = [10, 10]
    monster_1.equip_weapon("Short Sword")
    monster_1.condition["Hit Points"] = [12, 12]
    monster_1.condition["Magic Points"] = [10, 10]
    '''
    player_2.equip_weapon("Short Sword")
    player_1.equip_weapon("Unarmed")
    player_1.inspect_weapons()
    player_2.inspect_weapons()
    player_2.inspect_equipment()
    player_1.inspect_equipment()
    player_2.equip_weapon("Short Sword")
    '''
    # player_1.raise_skill("Accounting")
    # player_1.skills["Melee Weapon"][0] = 40
    # player_2.raise_skill("Melee Weapon")
    # player_1.inspect_skills()
    # player_1.check_current_condition()
    # player_1.take_damage(11)
    # player_1.take_damage(3)
    # player_1.check_current_condition()
    player_1.choose_action_explore()
    # player_1.check_current_condition()
    print("Works Fine 1")


if __name__ == "__main__":
    main()
