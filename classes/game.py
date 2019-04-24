import random

class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OFGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Person:
    def __init__(self, hp, mp, attack, df, magic):
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.attack_high = attack + 10
        self.attack_low = attack - 10
        self.magic = magic
        self.df = df
        self.act = ["Attack","Magic"]

    def generate_damage(self):
        return random.randrange(self.attack_low,self.attack_high)

    def get_hp(self):
        return self.hp

    def get_mp(self):
        return self.mp

    def reduce_mp(self, mp):
        self.mp = self.mp - mp

    def get_action_len(self):
        return len(self.act)

    def get_magic_len(self):
        return len(self.magic)

    def take_damage(self, dmg):
        self.hp = self.hp - dmg

    def heal_hp(self, heal_dmg):
        self.hp = self.hp + heal_dmg

    def choose_action(self):
        for i in range(len(self.act)):
            print(i+1,":",self.act[i])

    def get_action(self, ch):
        return self.act[ch]

    def choose_magic(self):
        for i in range(len(self.magic)):
            print(i+1,":",self.magic[i].get_magic_name())
