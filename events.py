import sys

from attributes import Creature


class New(Creature):
    ...

'''        
        def fight(self, monster):
        seq = self.combat_seq(monster)
        player_hp = self.condition["Hit Points"][0]
        monster_hp = monster.condition["Hit Points"][0]
        if seq == "1":
            message = f"You have an advantage in battle preparation's against {monster.creature[1]}"
        elif seq == "2":
            message = f"Look's like that {monster.creature[1]} is gonna attack you"
            monster.attack
            self.choose_action_defend()
        while True:
            try:
                pre_battle = int(input(f"{message}:\n"
                f"1. just start the rumble\n"
                f"2. try to make a surprise attack\n"
                f"3. cast a spell before battle\n"
                f"4. escape"))
                if pre_battle in (1,2,3,4):
                    return pre_battle
                else:
                    raise ValueError
            except ValueError:
                print(f"choose a number (numeric) from 1 to 4\n"
                      f"1. just start the rumble\n"
                      f"2. try to make a surprise attack\n"
                      f"3. cast a spell before battle\n"
                      f"4. escape")
                continue
    
        if pre_battle == 1 and condition == "def":
            is_hit = self.dice_success(monster,"str")
            evade = self.dice_success(player,"dex")
            if to_num(is_hit) > to_num(evade):
                print(f"The {monster.type} hit was success")
                damage = monster.hit(monster.weapon)
                player_hp -= damage
    
        elif pre_battle == 2:
            is_hit = dice_success(monster, "str")
            evade = dice_success(player, "dex")
            if to_num(is_hit) > to_num(evade)/2:
                print(f"The {monster.type} hit was success")
                damage = monster.hit(monster.weapon)
                player_hp -= damage
        elif pre_battle == 3:
            sorcery = input(f"Choose spell from list:\n"
                            f"{spell_list.split(',')}")
            if sorcery == "fire_ball":
                damage = fire_ball.action
                if damage[0] == "1":
                    damage_value = dice(int(damage[2]))
                elif damage[0] == "2":
                    damage_value = dice(int(damage[2])) + dice(int(damage[2]))
                elif damage[0] == "3":
                    damage_value = dice(int(damage[2])) + dice(int(damage[2])) + dice(int(damage[2]))

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
    player_1.up_hard = True
    monster_1.up_extreme = False
#    player_1.check_attack_success()
#    monster_1.check_fight_back_success()
    fighting_round(player_1, monster_1)
def fighting_round(player_1,player_2):
    if player_1.combat_seq(player_2) == "1":
        attacking = player_1
        defending = player_2
    else:
        attacking = player_2
        defending = player_1

    while attacking.condition["Death"] != ["DEAD"] or defending.condition["Death"] != ["DEAD"]:
        for i in range(attacking.apr):
            if attacking.condition["Death"] == ["DEAD"] or defending.condition["Death"] == ["DEAD"]:
                break
            i += 1
            acaa = attacking.choose_action_attack()
            dcad = defending.choose_action_defend()
            if attacking.success_to_num(acaa) > defending.success_to_num(dcad[0]):
                if dcad[1] == "D":
                    print(f"{defending.creature[0]} failed to dodge {attacking.creature[0]}'s attack")
                elif dcad[1] == "F":
                    print(f"{defending.creature[0]} failed fight back {attacking.creature[0]}'s attack")
                defending.take_damage(attacking.attack_value())
            else:
                if dcad[1] == "D":
                    print(f"{defending.creature[0]} successfully dodges {attacking.creature[0]}'s attack")
                elif dcad[1] == "F":
                    print(f"{defending.creature[0]} successfully fight back {attacking.creature[0]}'s attack\n"
                          f"amd now performs a counter attack...")
                    attacking.take_damage(defending.attack_value())
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print(f'Short battle report:\n'
                f'[{defending.creature[0]} HP: {defending.condition["Hit Points"]}] and ' \
                f'[{attacking.creature[0]} HP: {attacking.condition["Hit Points"]}]\n'\
                f'+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

        for i in range(defending.apr):
            if attacking.condition["Death"] == ["DEAD"] or defending.condition["Death"] == ["DEAD"]:
                break
            i += 1
            acaa = defending.choose_action_attack()
            dcad = attacking.choose_action_defend()
            if defending.success_to_num(acaa) > attacking.success_to_num(dcad[0]):
                attacking.take_damage(defending.attack_value())
            else:
                if dcad[1] == "D":
                    print(f"{attacking.creature[0]} successfully dodges {defending.creature[0]} attack")
                elif dcad[1] == "F":
                    defending.take_damage(attacking.attack_value())
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        if attacking.condition["Death"] == ["DEAD"] or defending.condition["Death"] == ["DEAD"]:
            if attacking.is_player and attacking.condition["Death"] == ["DEAD"]:
                sys.exit(f"{attacking.creature[0]} was killed by {defending.creature[0]}\n"
                         f"...........................................\n"
                         f"++++++++++++++++ Game Over ++++++++++++++++")
            elif attacking.is_player and defending.condition["Death"] == ["DEAD"] and attacking.condition["Death"] != ["DEAD"]:
                print(f"{attacking.creature[0]} successfully defeated {defending.creature[0]}\n"
                         f"...........................................\n"
                         f"!!!!!!!!!!!!! Congratulations !!!!!!!!!!!!!")
                return True
            elif defending.is_player and defending.condition["Death"] == ["DEAD"]:
                sys.exit(f"{defending.creature[0]} was killed by {attacking.creature[0]}\n"
                         f"...........................................\n"
                         f"++++++++++++++++ Game Over ++++++++++++++++")
            elif defending.is_player and attacking.condition["Death"] == ["DEAD"] and defending.condition["Death"] != ["DEAD"]:
                print(f"{defending.creature[0]} successfully defeated {attacking.creature[0]}\n"
                         f"...........................................\n"
                         f"!!!!!!!!!!!!! Congratulations !!!!!!!!!!!!!")
'''
            for "Fail" < "Regular success" < "Hard success" < "Extreme success":
                if attacking.attack_success() > defending.defence_success():
                    defending.take_damage(attacking.damage_value)
                else:
                    print("Failed to attack")
'''

'''    
    print(player_1.check_attack_success())
    print(player_1.check_fight_back_success())
    print(player_1.attack_value())
    print(player_2.attack_value())
    
'''
if __name__ == "__main__":
    main()
