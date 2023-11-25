class GeneratorIterable:
    def __iter__(self):
        return self.generator()

    def generator(self):
        yield from range(793)

iterable = GeneratorIterable()

for value in iterable:
    print(value)