from random import randint


class Buffer:
    def __init__(self):
        self.elements: list = list()
        self.sum_of_five_elements: int = 0

    def add(self, *a) -> None:
        for number in a:
            self.elements.append(number)

            if len(self.elements) == 5:
                for element in self.elements:
                    self.sum_of_five_elements += element
                self.elements.clear()
                print(f"Sum of five elements: {self.sum_of_five_elements}")
                self.sum_of_five_elements = 0

    def get_current_part(self) -> list:
        return self.elements


if __name__ == "__main__":
    buffer = Buffer()

    for i in range(10):
        elements: list = [randint(0, 15) for j in range(randint(1, 16))]
        print(f"Generated sequence: {elements}")
        buffer.add(*elements)
        print(f"Current part in buffer: {buffer.get_current_part()}")
