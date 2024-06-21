class Fibonacci:
    def __init__(self):
        self.lst = []
        self.a = 1
        self.b = 1
    def __iter__(self):
        return self
    def __next__(self):
        self.lst.append(self.a)
        f = self.a + self.b
        self.a = self.b
        self.b = f
        return self.lst[-1]

f = Fibonacci()
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))

