class Class:
    def __init__(self):
        self.value = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        alphabet = f"{self.index}{self.value[self.index]}"
        self.index = (self.index + 1)%len(self.value)
        return alphabet

f = Class()
for i in range(30):
    print(next(f), end="")