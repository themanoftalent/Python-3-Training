class fibon:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def series(self):
        while True:
            yield (self.b)
            self.a, self.b = self.b, self.a + self.b


f = fibon(0, 1)
for r in f.series():
    if r > 200:
        break
    print(r)
