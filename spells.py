import sys


class Spell:
    def __init__(self, type: str, action: str, element: str):
        self.type = type
        self.action = action
        self.element = element

    def __str__(self):
        result = str(self)
        print(f"{result}")



fire_ball = Spell("damage", "2D6+5", "fire")
ice_lance = Spell("damage", "3D5+2", "ice")
spell_list = "fire_ball, ice_lance"