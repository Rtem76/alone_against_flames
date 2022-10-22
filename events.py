import inspect

from dice import dice, dice_success
from spells import Spell
from spells import spell_list,fire_ball,ice_lance

def main():
    ...

def fight_1v1(player, monster, condition = "att"):
    if condition == "att":
        message = f"You have an advantage in battle preparation's against {monster.type}"
    elif condition == "def":
        message = f"Look's like that {monster.type} is gonna attack you"
    player_hp = player.hp
    monster_hp = monster.hp
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
        is_hit = dice_success(monster,"str")
        evade = dice_success(player,"dex")
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




if __name__ == "__main__":
    main()
