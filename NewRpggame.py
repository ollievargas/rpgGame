class Character:
    def __init__(self, health , power, name):
        self.health = health
        self.power = power
        self.name = name

    def alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def attack(self, enemy):
        enemy.health -= self.power
        print(f"The {self.name} inflicts {self.power} damage against the {enemy.name}")
        if enemy.health <= 0:
            print(f"The {enemy.name} is dead.")
        if self.health <= 0:
            print(f"The {self.name} is dead.")

    def print_status(self):
        print("{} has {} health and {} power.".format(self.name, self.health, self.power))



class Hero(Character):
    def __init__(self, health, power):
        self.name = "Hero"
        super().__init__(health, power, self.name)
        

class Goblin(Character):
    def __init__(self, health, power):
        self.name = "Goblin"
        super().__init__(health, power, self.name)
        


def main():
    hero1 = Hero(10,5)
    goblin1 = Goblin(6,2)

    while goblin1.alive() and hero1.alive():
        hero1.print_status()
        goblin1.print_status()
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        userInput = input()
        if userInput == "1":
            hero1.attack(goblin1)
        elif userInput == "2":
            pass
        elif userInput == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(userInput))

        if goblin1.health > 0:
            goblin1.attack(hero1)


main()