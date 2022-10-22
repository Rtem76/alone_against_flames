from atributes import Atributes, Weapons
from dice import dice_success, dice
#from weapons import Weapons
from events import fight_1v1


def main():
    short_sword = Weapons("Short Sword", "2D6", 20, "Sword", "One handed")
#    print(short_sword)
    short_bow = Weapons("Short Bow", "3D4+1", 80, "Bow", "Two handed")
    ork = Atributes(60,60,60,60,60,60,60,60,60,60,60,60,"ugly ork")
    ork.weapon = short_sword
    print(ork.weapon.name)
    albus = Atributes(60,60,60,60,60,60,60,60,60,60,60,60,"human")
    albus.weapon = short_bow
    print(albus.weapon.name)
    ork.upgrade_stat("hp", -26)
    ork.choose_weapon(short_bow)
    print(f" {ork.race} armed with {ork.weapon.name} and {albus.race} armed with {albus.weapon.name}")
    print(dice_success(ork,"con"))
    damage_deal = albus.weapon.dealt_damage(10)
    print(damage_deal, albus.weapon.name)



if __name__ == "__main__":
    main()