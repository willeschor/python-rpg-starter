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
    
    def special_inc (self, modifier):
        self.special_att += modifier
    
    def hit_chance (self):
        if random.randint(1,100) <= (30 + self.special_att):
            return True
        else:
            return False

    def status(self):
        return f"The {self.type_char} {self.name} has {self.power} power and {self.health:.0f} remaining. The special attribute is at {self.special_att}."

class Goblin(Character):
    def __init__(self, name, special_att, type_char, health, power):
        super().__init__(name, special_att, type_char, health, power)
    
    def war_cry(self):
        return "Garrragg!!"

    def gob_fart(self, other_char):
        if random.randint(1,5) > 4:
            other_char.special_att -= 5
            return "The Goblin farted... Gross\nYour heroism dropped by 5."

class Warrior(Character):
    def __init__(self, name, special_att, type_char, health, power):
        super().__init__(name, special_att, type_char, health, power)
    
    def increase_power (self):
        if self.special_att <= 5:
            return "You don't have enough heroism to increase your power"
        else:
            self.power += 5
            return f"Your power increased by 5 to {self.power}"
    
    def heal_self(self):
        self.health += self.special_att * 0.1
        return self.special_att * 0.1
        
    def war_cry(self):
        return "For Valhalla!!"
