# from random import randint, random

from models import Population


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


# age = 0
# health = 0
# while True:
#     age += 1
#     if age < 20:
#         health += 5
#     if 20 <= age < 35:
#         health += 8
#     if 35 <= age < 45:
#         health += 12
#     if 45 <= age < 55:
#         health += 15
#     if 55 <= age < 65:
#         health += 18
#     if age >= 65:
#         health += 25
#     if health >= 1000:
#         print(age)
#         break
    
