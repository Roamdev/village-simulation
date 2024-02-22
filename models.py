from random import randint
import names


class Person:
    def __init__(self, age=0, gender=True, best_friend=None):
        self.name = names.get_full_name()
        self.age = age
        self.gender = gender
        self.best_friend = best_friend
        self.alcohol = True

    def die(self):
        del self

new_person1 = Person(age=15)
new_person2 = Person(age=14, best_friend=new_person1)
print(new_person1.name)
print(randint(1, 666))

new_person1.die()
print(new_person2.name)


class Chif(Person):
    """pass"""
    pass
