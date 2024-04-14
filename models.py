from random import randint, random, choice
import names
import psycopg2


class Person:
    def __init__(self, newborn, population=None, best_friend=None):
        self.gender = choice(["male", "female"])
        self.name = names.get_full_name(gender=self.gender)
        self.population = population
        self.best_friend = best_friend
        self.alcohol = choice([True, False])
        self.death = False
        self.sport = False
        self.partner = None
        self.never_given_birth = None
        self.born_counter = 0
        percent_chance = randint(0, 100)
        if newborn and (percent_chance == 14 or percent_chance == 88):
            self.health = choice([999, 1000])
        else:
            self.health = randint(0, 500)
        if newborn:
            self.age = 0
        else:
            self.age = randint(18, 45)

    def person_change(self):
        thousand_chance = randint(0,1000)
        if thousand_chance == 666:
            self.death = True
        if thousand_chance <= 300:
            self.sport = True
        if thousand_chance > 300:
            self.sport = False
        if self.age > 13 and 250 <= thousand_chance <= 625:
            self.alcohol = True
        if thousand_chance > 625:
            self.alcohol = False
        if self.gender == 'female':
            if self.partner and thousand_chance > 950:
                self.partner = False
                self.partner.partner = False
            if self.never_given_birth and self.partner and self.born_counter < 3:
                self.born_counter += 1
            if self.born_counter == 3:
                self.population.population_list.append(Person(newborn=True, population=self.population))
                self.born_counter = 0

    def manage_health(self):
        if self.sport:
            sport_mod = randint(-6, -2)
        else:
            sport_mod = 0
        if self.alcohol:
            alcohol_mod = randint(-1, 6)
        else:
            alcohol_mod = 0
        self.age += 1
        if self.age < 20:
            self.health += 5 + sport_mod + alcohol_mod
        elif self.age < 35:
            self.health += 8 + int(sport_mod * 1.4) + int(alcohol_mod * 1.6)
        elif self.age < 45:
            self.health += 12 + int(sport_mod * 1.5) + int(alcohol_mod * 2)
        elif self.age < 55:
            self.health += 15 + int(sport_mod * 1.6) + int(alcohol_mod * 2.4)
        elif self.age < 65:
            self.health += 18 + int(sport_mod * 1.7) + int(alcohol_mod * 3)
        elif self.age >= 65:
            self.health += 25 + int(sport_mod * 1.4) + int(alcohol_mod * 3)
        if self.health >= 1000:
            self.death = True
    
    def die(self):
        del self


class Population:
    def __init__(self, name, population_growth=None):
        self.population_list = []
        self.name = name
        for i in range(150):
            new_person = Person(newborn=False)
            self.population_list.append(new_person)
        self.population_growth = population_growth


        # conn = psycopg2.connect(dbname="postgres", user="postgres", password="123456", host="127.0.0.1", port="5432")
        # print("Подключение установлено")

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
