def dis(self):
    for k, v in enumerate(self.__dict__):
        return k, v
Pet = type("Pet", (), {"dis":dis, "name":"Tom", "age":7})
my_pet = Pet()
print(my_pet.dis())
