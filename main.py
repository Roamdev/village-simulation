from random import randint, random


from models import Population, Person


def change_year(village, village_name):
    year = 0
    while year <= 1:
        print(f'year: {year}')
        year += 1
        village.growth_population()
        print(f'in {village_name}: {len(village.population_list)} '
              f'(+{village.population_growth} in a year)')


change_year(Population(), 'Villariba')
change_year(Population(), 'Villabajo')
