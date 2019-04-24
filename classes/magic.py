import random

class Magic:

    def __init__(self, name, cost, dmg, typ):
        self.name = name 
        self.cost = cost
        self.dmg = dmg
        self.type = typ

    def generate_damage(self):
        low = int(self.dmg) - 20
        high = int(self.dmg) + 20
        return random.randrange(low,high)
    

    def get_magic_name(self):
        return self.name

    def get_magic_cost(self):
        return int(self.cost)

    def get_magic_dmg(self):
        return int(self.dmg)

    def get_magic_type(self):
        return self.type