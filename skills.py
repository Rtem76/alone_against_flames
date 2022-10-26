import copy

# skills dictionary => skill aka key: [value, mastering, "description"]

skills_initial = {
    "Accounting": [10, None],
    "Anthropology": [1, None],
    "Archaeology": [1, None],
    "Art": [5, None],
    "Astronomy": [1, None],
    "Bargain": [5, None],
    "Biology": [1, None],
    "Chemistry": [1, None],
    "Climb": [40, None],
    "Conceal": [15, None],
    "Craft": [5, None],
    "Credit Rating": [15, None],
    "Disguise": [1, None],
    "Dodge": [10, None],
    "Drive Automobile": [20, None],
    "Electrical Repair": [10, None],
    "Fast Talk": [5, None],
    "First Aid": [30, None],
    "Fist/Punch": [50, None],
    "Geology": [1, None],
    "Grapple": [25, None],
    "Handgun": [20, None],
    "Head Butt": [10, None],
    "Hide": [10, None],
    "History": [20, None],
    "Jump": [25, None],
    "Kick": [25, None],
    "Law": [10, None],
    "Library Use": [25, None],
    "Listen": [25, None],
    "Locksmith": [1, None],
    "Machine Gun": [15, None],
    "Martial Arts": [1, None],
    "Mechanical Repair": [20, None],
    "Medicine": [5, None],
    "Natural History": [10, None],
    "Navigate": [10, None],
    "Occult": [5, None],
    "Operate Heavy Machine": [1, None],
    "Other Language": [1, None],
    "Own Language": [5, None],
    "Persuade": [15, None],
    "Pharmacy": [1, None],
    "Photography": [10, None],
    "Physics": [1, None],
    "Pilot": [1, None],
    "Psychoanalysis": [1, None],
    "Psychology": [5, None],
    "Ride": [5, None],
    "Rifle": [25, None],
    "Shotgun": [30, None],
    "Sneak": [10, None],
    "Spot Hidden": [25, None],
    "Submachine Gun": [15, None],
    "Swim": [25, None],
    "Throw": [25, None],
    "Track": [10, None],
    "Melee Weapon": [70, None],
}
#p1_skills = copy.deepcopy(skills_initial)
#p2_skills = copy.deepcopy(skills_initial)

class Skills():
    def __init__(self, skills: dict):
        self.skills = skills

    def __str__(self):
        result = str(self)
        print(f"{result}")

    def find_skill_value(self, skill_name):
        return self.skills[skill_name][0]

    def raise_skill(self, skill_name):
        result_of_dice = dice(100)
        current = self.find_skill_value(skill_name)
        if result_of_dice > current:
            if result_of_dice >= current + 10:
                current += 10
            else:
                current = result_of_dice
            print(f"Congratulation's your skill of {skill_name} rises to {current}")
            self.skills[skill_name][0] = current
def main():
    mario = Skills(copy.deepcopy(skills_initial))
    any = Skills(copy.deepcopy(skills_initial))
    any.raise_skill("Accounting")
    mario.skills["Melee Weapon"][0] = 40
    mario.raise_skill("Melee Weapon")
    print(f' Now Any have {any.find_skill_value("Accounting")} point in Acoounting skill')
    print(f' Now Mario have {mario.find_skill_value("Accounting")} point in Acoounting skill')
    print(f' Now Any have {any.find_skill_value("Melee Weapon")} point in Melee weapon skill')
    print(f' Now Mario have {mario.find_skill_value("Melee Weapon")} point in Melee weapon skill')
    # skills dictionary => skill aka key: [value, mastering, "description"]

if __name__ == "__main__":
    main()