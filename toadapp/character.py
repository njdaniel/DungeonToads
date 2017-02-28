#character.py

class Character(object):
    def __init__(self):
        self.name = ''
        self.strength = 0
        self.dexterity = 0
        self.constitution = 0
        self.intelligence = 0
        self.wisdom = 0
        self.charisma = 0
        self.health = 40
        self.points = 20
        self.moves = ['attack', 'dodge', 'block']
        print("Created character... almost")

# =================== Methods for Character ======================

