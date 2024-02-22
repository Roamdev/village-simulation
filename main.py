from random import randint

from models import Person, Chif



year = 0
population = []
while 5:
    print('year: ' + str(year))
    year += 1
    population_growth = randint(0, 50)
    
    for i in range(population_growth):
        new_person = Person(age=0)
        population.append(new_person)
    print(len(population) )





