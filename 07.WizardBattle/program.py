import random
import time

from actors import Wizard, Creature, smallCreature, dragon


def main():
    printHeader()
    gameLoop()


def printHeader():
    print("---------------------------------")
    print("         Wizard Battle")
    print("---------------------------------")
    print()


def gameLoop():

    creatures = [smallCreature('Toad', 1),
                 smallCreature('Bat', 3),
                 Creature('Tiger', 12),
                 dragon('Dragon', 50, 50, True),
                 Wizard('Evil Wizard', 1000)]

    hero = Wizard('Gregory', 75)

    while True:

        activeCreature = random.choice(creatures)

        print("A level {} {} appears in the mist..".format(activeCreature.level, activeCreature.name))
        print()

        cmd = input("Do you want to [a]ttack, [r]un away, or [l]ook around? ")
        if cmd == 'a':
            if hero.attack(activeCreature):
                creatures.remove(activeCreature)
            else:
                print("The hero must rest to regain his wits..")
                time.sleep(5)
                print("..Wizard {} returns with vigor!".format(hero.name))

        elif cmd == 'r':
            print("Wizard {} takes the tranquil path.".format(hero.name))

        elif cmd == 'l':
            print("Wizard {} scries the mist to find..".format(hero.name))
            for c in creatures:
                print(" *A level {} {}".format(c.level, c.name))

        else:
            print("Okay, see you next time.")
            break


if __name__ == '__main__':
    main()
