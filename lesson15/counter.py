class Counter:
    def __init__(self, start: int, stop: int):
        self.start = start
        self.current = self.start
        self.stop = stop

    def tick(self) -> int:
        pass

    def get_current(self) -> int:
        pass
