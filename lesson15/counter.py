"""
Exposes small and neat Counter class.
Counter ticking from start to stop value. During each tick Counter returns
current value.
"""


class Counter:
    def __init__(self, start: int, stop: int):
        """
        Creates Counter's object with start-stop values.

        :param start: number where to start ticking
        :param stop: last possible counter value, impossible to get higher value
        """
        self.start = start
        self.current = self.start
        self.stop = stop

    def tick(self) -> int:
        """
        Increments current value until it equals stop attribute.

        :return: current counter's value
        """
        if self.current < self.stop:
            self.current += 1
            return self.current

        return self.current

    def get_current(self) -> int:
        """
        Current getter method.

        :return: current value
        """
        return self.current


if __name__ == "__main__":
    counter = Counter(1, 10)

    print(counter.get_current())

    for i in range(counter.stop + 5):  # Trying to tick higher than stop value
        print(counter.tick())
