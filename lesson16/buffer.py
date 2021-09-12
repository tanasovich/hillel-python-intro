"""
Exposes Buffer class.
Buffer can add numeric sequence and get sum of each five elements.
"""
from random import randint


class Buffer:
    def __init__(self):
        """
        Creates Buffer object.
        """
        self.elements: list = list()
        self.sum_of_five_elements: int = 0

    def add(self, *a) -> None:
        """
        Adds numeric sequence to buffer. Prints sum of each five elements and
        remove them from the buffer.

        :param a: elements to be added to internal buffer
        :return: None
        """
        for number in a:
            self.elements.append(number)

            if len(self.elements) == 5:
                for element in self.elements:
                    self.sum_of_five_elements += element
                self.elements.clear()
                print(f"Sum of five elements: {self.sum_of_five_elements}")
                self.sum_of_five_elements = 0

    def get_current_part(self) -> list:
        """
        Gets current elements in buffer.

        :return: list of elements
        """
        return self.elements


if __name__ == "__main__":
    buffer = Buffer()

    for i in range(10):
        elements: list = [randint(0, 15) for j in range(randint(1, 16))]
        print(f"Generated sequence: {elements}")
        buffer.add(*elements)
        print(f"Current part in buffer: {buffer.get_current_part()}")
