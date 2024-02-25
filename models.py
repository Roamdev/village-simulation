from random import randint, random, choice
import names


class Person:
    def __init__(self, newborn, best_friend=None):
        self.name = names.get_full_name(gender=choice(["male", "female"]))
        self.best_friend = best_friend
        self.alcohol = True
        if newborn:
            self.age = 0
        else:
            self.age = randint(18,45)
        
    def init_age(self):
        self.__init__()

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
            newborn_chance = random()
            if newborn_chance > .3:
                newborn_chance = True
            else:
                newborn_chance = False
            new_person = Person(newborn=newborn_chance)
            self.population_list.append(new_person)
class Chief(Person):
    """pass"""
    pass
