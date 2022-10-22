#from dice import dice

class Skills:
    def __init__(self, skill_name: int, proficiency: int, mastered = None):
        self.skill_name = skill_name
        self.proficiency = proficiency
        self.mastered = mastered
        if self.proficiency >= self.mastered
            self.mastered = self.proficiency

    def __str__(self):
        result = str(self)
        print(f"{result}")



    def raise_skill(self, stat):
        if stat == "accounting":
            result_of_dice = dice(100)
            if result_of_dice > self.accounting:
                if result_of_dice >= self.accounting + 10:
                    self.accounting +=10
                else:
                    self.accounting = dice
                print(f"Congratulation's your skill of accounting rises to {self.accounting}")

        elif stat == "athletics":
            result_of_dice = dice(100)
            if result_of_dice > self.athletics:
                if result_of_dice >= self.athletics + 10:
                    self.athletics +=10
                else:
                    self.athletics = dice
            elif stat == "one_handed":
                result_of_dice = dice(100)
                if result_of_dice > self.one_handed:
                    if result_of_dice >= self.one_handed + 10:
                        self.one_handed +=10
                    else:
                        self.athletics = dice
            elif stat == "two_handed":
                result_of_dice = dice(100)
                if result_of_dice > self.two_handed:
                    if result_of_dice >= self.two_handed + 10:
                        self.two_handed += 10
                    else:
                        self.athletics = dice
        else:
            print("can't modify that value")

def class Mastered(Skills):
    def __init__(self, mastered: int):
        self.mastered = mastered
        super().__init__(skill_name=self)


any = Skills(10,10,10,10)
any.raise_skill("accounting")

print(any.accounting)