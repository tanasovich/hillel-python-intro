import random

natural_numbers: list = [random.randrange(0, 100) for i in range(15)]

k: int = int(input("Enter index k (0 <= k < 15): "))

for i in range(k, len(natural_numbers)-1):
    natural_numbers[i], natural_numbers[i+1] = natural_numbers[i+1], natural_numbers[i]

natural_numbers.pop()

print(natural_numbers)
