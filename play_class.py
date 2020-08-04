import random
class Character():
    def __init__(self, name, special_att , type_char, health, power ):
        self.health = health
        self.power = power
        self.name = name
        self.type_char = type_char
        self.special_att = special_att
    
    def mod_health(self, num):
        self.health -= num
    
    def heal_self(self):
        self.health += self.special_att * 0.1
        return self.special_att * 0.1

    def special_inc (self, modifier):
        self.special_att += modifier
    
    def hit_chance (self):
        if random.randint(1,100) <= (0 + self.special_att):
            return True
        else:
            return False

    def __str__(self):
        return f"The {self.type_char} {self.name} has {self.power} power and {self.health} remaining."

class Goblin(Character):
    def __init__(self, name, special_att, type_char, health, power):
        super().__init__(name, special_att, type_char, health, power)
    
    def war_cry(self):
        return "Garrragg!!"


class Warrior(Character):
    def __init__(self, name, special_att, type_char, health, power):
        super().__init__(name, special_att, type_char, health, power)
    
    def war_cry(self):
        return "For Valhalla!!"
