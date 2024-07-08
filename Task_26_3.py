class Person:
    def __init__(self, age):
        self._age = age
        pass
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, age):
        if 1 < age < 100:
            return self._age
        else:
            print("Недопустимый возраст")
            self._age = str(age)

tom = Person(128)
print(tom.age)