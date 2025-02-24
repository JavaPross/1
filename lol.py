class IterableWithGenerator:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        def generator():
            for i in range(self.start, self.stop):
                yield i
        return generator()

iterable = IterableWithGenerator(1, 5)

for value in iterable:
    print(value)
