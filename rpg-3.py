
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
    warrior_jim = Warrior('Jim', 10, 'Warrio', 50, 5)
    gob_bob = Goblin('Bob', 10, 'Goblin',50, 5)
    print(f"You walk down the path a proud {warrior_jim}.")
    print(f"Suddenly, you see a {gob_bob}")

    while warrior_jim.health > 0 and gob_bob.health > 0:
        
        print("What do you want to do?")
        print(f"1. Fight {gob_bob.type_char} {gob_bob.name}")
        print(f"2. Heal")
        print(f"3. Cast Reduce Attribute")
        print(f"4. Increase Power")
        print(f"5. Flee")
        print(f"> ", end='')
        
        while incorrect == 1:
            user_input = int(input())
            if user_input <= 5:
                incorrect = 0
            else:
                print("That's not a good choice.\nTry again.")

        if user_input == 1:
            # Hero attacks goblin
            if(warrior_jim.hit_chance()):
                print(f"Hit landed! You did {warrior_jim.power} damage.")
                gob_bob.mod_health(warrior_jim.power)
                warrior_jim.special_inc(5)
                print(warrior_jim.war_cry())
            else:
                print("Swing and a miss...")
                warrior_jim.special_inc(-1)

        elif user_input == 2:
            print(f"You healed for {warrior_jim.heal_self()}")

        elif user_input == 3:
            gob_bob.special_inc(-2)
            print(f"You cast an attribute reduction on {gob_bob.name}.")
            print(f"{gob_bob.name}'s ugliness is now at {gob_bob.special_att}.")
        
        elif user_input == 4:
            print("I have the power!!!")
            print(warrior_jim.increase_power())
        else:
            print("You ran away... sad.")
            break

        if gob_bob.health > 0:
            # Goblin attacks hero
            print("Goblin attacks!")
            if(gob_bob.hit_chance()):
                print(f"Hit landed! {gob_bob.name} did {gob_bob.power} damage.")
                warrior_jim.mod_health(gob_bob.power)
                gob_bob.special_inc(5)
                print(gob_bob.war_cry())
            else:
                print("Swing and a miss...")
                gob_bob.special_inc(-1)
                gob_bob.gob_fart(warrior_jim)
        else:
            print(f"You defeated {gob_bob.type_char} {gob_bob.name}")
            break   
        
        if warrior_jim.health <= 0:
                print("The Goblin defeated you. Sad.")
                break
        print(warrior_jim.status())
        print(gob_bob.status())

        user_input = 0
        incorrect = 1
main()
