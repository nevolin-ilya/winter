class Person:
    def __init__(self, name, halfname, surname):

        self.name = name
        self.halfname = halfname
        self.surname = surname
    def __str__(self):

        return f"Person({self.surname[::-1]}{self.halfname[::-1]}{self.name[::-1]})"
p = Person("Неволин", "Илья", "Сергеевич")

print(p)