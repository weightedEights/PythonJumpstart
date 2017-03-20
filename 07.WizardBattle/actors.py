import random


class Creature:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):
        return "Creature: {}, level {}".format(
            self.name, self.level
        )

    def defensiveRoll(self):
        return random.randint(1, 12) * self.level


class Wizard(Creature):
    def attack(self, creature):
        print("The wizard {} attacks {}!".format(self.name, creature.name))

        heroRoll = self.defensiveRoll()
        print("Hero rolls {}".format(heroRoll))
        creatureRoll = creature.defensiveRoll()
        print("Creature rolls {}".format(creatureRoll))

        if heroRoll >= creatureRoll:
            print("The hero dispatches the {} with aplomb.".format(creature.name))
            return True
        else:
            print("This hero's mettle was insufficient.")
            return False


class smallCreature(Creature):
    def defensiveRoll(self):
        # small creatures have 0.5x size penalty
        return super().defensiveRoll() * 0.5


class dragon(Creature):
    def __init__(self, name, level, scaliness, breathsFire):
        super().__init__(name, level)
        self.breathsFire = breathsFire
        self.scaliness = scaliness

    def defensiveRoll(self):
        baseRoll = super().defensiveRoll()

        # dragons have 1.5x size advantage
        sizeModifier = 1.5

        # if dragon breathes fire
        fireModifier = 5 if self.breathsFire else 1

        # dragons have armor too
        scalyModifier = self.scaliness / 10

        return baseRoll * sizeModifier * fireModifier * scalyModifier

