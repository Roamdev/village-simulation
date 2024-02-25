from random import randint, random

from models import Person, Population


year = 0
velaribo = Population()

while year <= 10:
    print('year: ' + str(year))
    year += 1
    velaribo.growth_population()
    print(str(len(velaribo.population_list)) + ': (+' + str(velaribo.population_growth) + ')')
