# class Item:
#     def __init__(self, name, price, quantity, total):
#         self.name = name.title()
#         self.price = price
#         self.quantity = quantity
#         self.total = total
#     def __getattribute__(self, attr):
#         if attr == self.total:
#             return self.price * self.quantity
#         else:
#             #print(f"Значение атрибута: {attr}")
#             return object.__getattribute__(self, attr)
#
# f = Item('ilya', 10, 100)
# print(f.name)

class Item:
    def __init__(self, **kwargs):
        self.kw = kwargs
        # for k, v in kwargs.items():
        #     self.__dict__[k] = v

    def __str__(self):

        for k, v in self.__dict__.items():
            if k == name:
                return str(v).title()
            if k == total:
                res =
                return


ac = Item(name = 'Murka', price = 45, quantity = 123)
print(ac.name)