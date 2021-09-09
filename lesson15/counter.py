class Counter:
    def __init__(self, start: int, stop: int):
        self.start = start
        self.current = self.start
        self.stop = stop

    def tick(self) -> int:
        if self.current < self.stop:
            self.current += 1
            return self.current
        else:
            return self.current

    def get_current(self) -> int:
        return self.current


if __name__ == "__main__":
    counter = Counter(1, 10)

    print(counter.get_current())

    for i in range(counter.stop + 5):  # Trying to tick higher than stop value
        print(counter.tick())
