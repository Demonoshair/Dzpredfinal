class Counter:
    current: int

    def __init__(self, flag=True):
        self.current = 0
        self.flag = flag

    def __str__(self):
        return self.current

    def __iter__(self):
        return self

    def __next__(self):
        current = self.current
        self.current = self.current + 1 if self.flag else self.current - 1
        return current


c = Counter()
i = iter(c)

while True:
    if input() == "exit":
        break
    print(next(i))