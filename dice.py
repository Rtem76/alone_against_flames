import random


def main():
    ...

def dice(num):
    if num in (4,6,8,20):
        result = random.randrange(1, num)
        print(f"Result of {num} sided knuckle dice is {result}")
        return result
    elif num == 100:
        first_dice = random.randrange(0,9)
        second_dice = random.randrange(0,9)
        print(f"The ten's dice is {first_dice} and unit dice is {second_dice}")
        result = int(str(first_dice)+str(second_dice))
        if result == 0:
            result = 100
        print(result)
        return result

def dice_success(player, stat):
    num = dice(100)
    chosen_stat = player.choose_stat(stat)
    if num <= chosen_stat/5:
        return "Extreme success"
    elif num <= chosen_stat/2:
        return "Hard success"
    elif num <= chosen_stat:
        return "Regular success"
    else:
        return "Failed"


if __name__ == "__main__":
    main()