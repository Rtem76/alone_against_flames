import sys

from attributes import Creature


class New(Creature):
    ...




def main():
    monster_1 = Creature(False, "Murche Barca Keen", "goblin")
    player_1 = Creature(True, "Alex", "human")
    monster_2 = Creature(False, "Dendrakis", "orc")
    player_1.equip_weapon("Short Sword")
    player_1.condition["Hit Points"] = [33, 33]
    player_1.condition["Magic Points"] = [10, 10]
    monster_1.equip_weapon("Short Sword")
    monster_1.condition["Hit Points"] = [12, 12]
    monster_1.condition["Magic Points"] = [10, 10]
    monster_1.up_extreme = False
    monster_2.equip_weapon("Short Sword")
    monster_2.condition["Hit Points"] = [20, 20]
    monster_2.condition["Magic Points"] = [10, 10]
    monster_2.up_extreme = False
    player_1.skills["Melee Weapon"][1] = True
    player_1.skills["Melee Weapon"][0] = 55
    #    player_1.check_attack_success()
    #    monster_1.check_fight_back_success()
    fighting_round(player_1, monster_1, 1)
    fighting_round(player_1, monster_2, 1)


def fighting_round(player_1, player_2, distance: int):
    if player_1.combat_seq(player_2) == "1":
        attacking = player_1
        defending = player_2
    else:
        attacking = player_2
        defending = player_1

    while True:
        for i in range(attacking.apr):
            if attacking.condition["Death"] in ["DEAD","Knocked Out","Dying"] or defending.condition["Death"] in ["DEAD","Knocked Out","Dying"]:
                break
            else:
                i += 1
                acaa = attacking.choose_action_attack()
                dcad = defending.choose_action_defend()
                if attacking.success_to_num(acaa) >= defending.success_to_num(dcad[0]) and dcad[1] == "F":
                    if attacking.success_to_num(acaa) >= 1:
                        print(f"{defending.creature[0]} failed fight back {attacking.creature[0]}'s attack")
                        if acaa != "Failed" and acaa != "Extreme success":
                            defending.take_damage(attacking.attack_value())
                        elif acaa == "Extreme success":
                            defending.take_damage(attacking.critical_value())
                    else:
                        print(f"{attacking.creature[0]} failed to perform attack")
                elif attacking.success_to_num(acaa) > defending.success_to_num(dcad[0]) and dcad[1] == "D":
                    print(f"{defending.creature[0]} failed to dodge {attacking.creature[0]}'s attack")
                    if acaa == "Extreme success":
                        defending.take_damage(attacking.critical_value())
                    else:
                        defending.take_damage(attacking.attack_value())
                else:
                    if dcad[1] == "D":
                        print(f"{defending.creature[0]} successfully dodges {attacking.creature[0]}'s attack")
                    elif dcad[1] == "F":
                        print(f"{defending.creature[0]} successfully fight back {attacking.creature[0]}'s attack\n"
                              f"amd now performs a counter attack...")
                        if dcad[0] == "Extreme success":
                            attacking.take_damage(defending.critical_value())
                        else:
                            attacking.take_damage(defending.attack_value())
                if attacking.condition["Death"] in ["DEAD","Knocked Out","Dying"] or defending.condition["Death"] in ["DEAD","Knocked Out","Dying"]:
                    break
                print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                print(f'Short battle report:\n'
                      f'[{defending.creature[0]}] [{defending.condition["Hit Points"][0]}/{defending.condition["Hit Points"][1]}]'
                      f' {defending.condition["Death"]} and in {distance} feets away '
                      f'[{attacking.creature[0]}] [{attacking.condition["Hit Points"][0]}/{attacking.condition["Hit Points"][1]}]'
                      f' {attacking.condition["Death"]}\n'
                      #                f'{defending.print_name_hp} and in {distance} feets away '
                      #                f'{attacking.print_name_hp}\n'\
                      f'+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        for i in range(defending.apr):
            if attacking.condition["Death"] in ["DEAD","Knocked Out","Dying"] or defending.condition["Death"] in ["DEAD","Knocked Out","Dying"]:
                break
            else:
                i += 1
                acaa = defending.choose_action_attack()
                dcad = attacking.choose_action_defend()
                if defending.success_to_num(acaa) >= attacking.success_to_num(dcad[0]) and dcad[1] == "F":
                    if defending.success_to_num(acaa) >= 1:
                        print(f"{attacking.creature[0]} failed fight back {defending.creature[0]}'s attack")
                        if acaa != "Failed" and acaa != "Extreme success":
                            attacking.take_damage(defending.attack_value())
                        elif acaa == "Extreme success":
                            attacking.take_damage(defending.critical_value())
                    else:
                        print(f"{defending.creature[0]} failed to perform attack")
                elif defending.success_to_num(acaa) > attacking.success_to_num(dcad[0]) and dcad[1] == "D":
                    print(f"{attacking.creature[0]} failed to dodge {defending.creature[0]}'s attack")
                    if acaa == "Extreme success":
                        attacking.take_damage(defending.critical_value())
                    else:
                        attacking.take_damage(defending.attack_value())
                else:
                    if dcad[1] == "D":
                        print(f"{attacking.creature[0]} successfully dodges {defending.creature[0]}'s attack")
                    elif dcad[1] == "F":
                        print(f"{attacking.creature[0]} successfully fight back {defending.creature[0]}'s attack\n"
                              f"amd now performs a counter attack...")
                        if dcad[0] == "Extreme success":
                            defending.take_damage(attacking.critical_value())
                        else:
                            defending.take_damage(attacking.attack_value())
                if attacking.condition["Death"] in ["DEAD","Knocked Out","Dying"] or defending.condition["Death"] in ["DEAD","Knocked Out","Dying"]:
                    break
                print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                print(f'Short battle report:\n'
                    f'[{defending.creature[0]}] [{defending.condition["Hit Points"][0]}/{defending.condition["Hit Points"][1]}]'
                    f' {defending.condition["Death"]} and in {distance} feets away '
                    f'[{attacking.creature[0]}] [{attacking.condition["Hit Points"][0]}/{attacking.condition["Hit Points"][1]}]'
                    f' {attacking.condition["Death"]}\n'
                    f'+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        if attacking.condition["Death"] in ["DEAD","Knocked Out","Dying"] or defending.condition["Death"] in ["DEAD","Knocked Out","Dying"]:
            if attacking.is_player and (attacking.condition["Death"] in ["DEAD","Knocked Out","Dying"]):
                sys.exit(f"{attacking.creature[0]} was killed by {defending.creature[0]}\n"
                         f"...........................................\n"
                         f"++++++++++++++++ Game Over ++++++++++++++++")
            elif attacking.is_player and defending.condition["Death"] == "DEAD":
                print(f"{attacking.creature[0]} successfully defeated {defending.creature[0]}\n"
                      f"...........................................\n"
                      f"!!!!!!!!!!!!! Congratulations !!!!!!!!!!!!!")
                return True
            elif defending.is_player and (defending.condition["Death"] in ["DEAD","Knocked Out","Dying"]):
                sys.exit(f"{defending.creature[0]} was killed by {attacking.creature[0]}\n"
                         f"...........................................\n"
                         f"++++++++++++++++ Game Over ++++++++++++++++")
            elif defending.is_player and attacking.condition["Death"] == "DEAD":
                print(f"{defending.creature[0]} successfully defeated {attacking.creature[0]}\n"
                      f"...........................................\n"
                      f"!!!!!!!!!!!!! Congratulations !!!!!!!!!!!!!")
                return True

'''
            for "Fail" < "Regular success" < "Hard success" < "Extreme success":
                if attacking.attack_success() > defending.defence_success():
                    defending.take_damage(attacking.damage_value)
                else:
                    print("Failed to attack") 
                    
                    
                f'{defending.print_name_hp} and in {distance} feets away '
                f'{attacking.print_name_hp}'
                
                
    print(player_1.check_attack_success())
    print(player_1.check_fight_back_success())
    print(player_1.attack_value())
    print(player_2.attack_value())
    
'''
if __name__ == "__main__":
    main()
