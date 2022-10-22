import math
import random,sys


class Atributes:
    def __init__(self, str: int, con: int, dex: int, int: int, wis: int, chr: int, overview: str = ""):
        self.str = str
        self.vit = con
        self.dex = dex
        self.int = int
        self.wis = wis
        self.chr = chr
        self.overview = overview


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
        elif stat == "wis":
            return self.wis
        elif stat == "chr":
            return self.chr
        elif stat == "overview":
            return self.overview
        else:
            sys.exit("bug in choose_stat")



def charge_solo(player, stat, diff = 4):
    print(player.choose_stat(stat))
    if modify(player.choose_stat(stat)) >= diff:
        return True
    else:
        return False


def whats_next_events(num,move):
    step = random.randrange(0,3)
    move +=1
    if step == 0:
        print("take some rest")
        return (0,move)
    elif step == 1:
        print("that's an ambush")
        return (1,move)
    elif step == 2:
        print("look's like you found something")
        return (2,move)
    elif step == 3:
        print("someone is awaits you on next move")
        return (3,move)

def bad_event(num,move):
    step = random.randrange(0, 3)
    move +=1
    if step == 0:
        print("oh look's like you was lucky")
        return (0,move)
    elif step == 1:
        print("might be worse")
        return (1,move)
    elif step == 2:
        print("now it's become serious")
        return (2,move)
    elif step == 3:
        print("%%% happens")
        return (3,move)

def found_event(num,move):
    step = random.randrange(0, 3)
    move +=1
    if step == 0:
        print("oh look's like you was lucky")
        return (0,move)
    elif step == 1:
        print("that's nothing there, but it could be worse")
        return (1,move)
    elif step == 2:
        print("don't give up, try to dig deeper")
        return (2,move)
    elif step == 3:
        print("%%% happens")
        return (3,move)


def charge_vs(player_1, player_2, stat):
    if modify(player_1.choose_stat(stat)) >= modify(player_2.choose_stat(stat)):
        return True
    else:
        return False


def modify(stat: int, special: int = 0):
    result = math.ceil((stat - 10 + random.randrange(1,20))/2) + special
    print(result)
    return result


def main():
    ork = Atributes(16,8,12,12,12,12)
    maximus = Atributes(12,10,14,14,14,12)
    choosen_stat = "str"
    #print(charge_solo(maximus,choosen_stat))
    print(charge_vs(maximus,ork,choosen_stat))


if __name__ == "__main__":
    main()