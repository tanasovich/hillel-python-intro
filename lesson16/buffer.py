class Buffer:
    def __init__(self):
        self.elements: list = list()
        self.sum_of_five_elements: int = 0

    def add(self, *a):
        for number in a:
            self.elements.append(number)

            if len(self.elements) == 5:
                for element in self.elements:
                    self.sum_of_five_elements += element
                self.elements.clear()
                print(f"Sum of five elements: {self.sum_of_five_elements}")
                self.sum_of_five_elements = 0

    def get_current_part(self):
        pass
