
from play_class import Character
from play_class import Goblin
from play_class import Warrior
"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""

def main():
    incorrect = 1
    warrior_jim = Warrior('Jim', 20, 'Warrio', 50, 5)
    gob_bob = Goblin('Bob',20, 'Goblin',50,5)
    print(f"You walk down the path a proud {warrior_jim}.")
    print(f"Suddenly, you see a {gob_bob}")

    while True:
    #warrior_jim.health > 0 and gob_bob.health > 0:
        
        print("What do you want to do?")
        print(f"1. Fight {gob_bob.type_char} {gob_bob.name}")
        print(f"2. Heal")
        print(f"3. flee")
        print(f"> ",)
        
        while incorrect == 1:
            user_input = int(input())
            if user_input == 1 or user_input ==2 or user_input ==3:
                incorrect = 0
            else:
                print("That's not a good choice.\nTry again.")

        if user_input == 1:
            # Hero attacks goblin
            if(warrior_jim.hit_chance()):
                print(f"Hit landed! You did {warrior_jim.power} damage.")
                gob_bob.mod_health(warrior_jim.power)
                warrior_jim.special_inc(5)
            else:
                print("Swing and a miss...")
                warrior_jim.special_inc(-5)

        elif user_input == 2:
            print(f"You healed for {warrior_jim.heal_self()}")

        else:
            print("You ran away... sad.")
            break

        if gob_bob.health > 0:
            # Goblin attacks hero
            if(gob_bob.hit_chance()):
                print(f"Hit landed! You did {gob_bob.power} damage.")
                warrior_jim.mod_health(gob_bob.power)
                gob_bob.special_inc(5)
            else:
                print("Swing and a miss...")
                gob_bob.special_inc(-5)
        else:
            print(f"You defeated {gob_bob.type_char} {gob_bob.")
            break   
        if hero_health <= 0:
                print("You are dead.")

main()
