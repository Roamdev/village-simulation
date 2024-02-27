from random import randint, random, choice
import names


class Person:
    def __init__(self, newborn, best_friend=None):
        self.name = names.get_full_name(gender=choice(["male", "female"]))
        self.best_friend = best_friend
        self.alcohol = choice([True, False])
        self.death = False
        percent_chance = randint(0, 100)
        if newborn and (percent_chance == 14 or percent_chance == 88):
            self.health = choice([999, 1000])
        else:
            self.health = randint(0, 500)
        if newborn:
            self.age = 0
        else:
            self.age = randint(18, 45)

    def die(self):
        del self


class Population:
    def __init__(self, population_growth=None):
        self.population_list = []
        for i in range(150):
            new_person = Person(newborn=False)
            self.population_list.append(new_person)
        self.population_growth = population_growth

    def growth_population(self):
        self.population_growth = randint(int(len(self.population_list) * .1), int(len(self.population_list) * .3))
        for i in range(self.population_growth):
            migrant_chance = random()
            newborn = True
            if migrant_chance < .2:
                newborn = False
            new_person = Person(newborn=newborn)
            self.population_list.append(new_person)


class Chief(Person):
    """pass"""
    pass
