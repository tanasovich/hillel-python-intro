import random

natural_numbers: list = [random.randrange(0, 100) for i in range(15)]

k: int = int(input("Enter index k (0 <= k < 15): "))
c: int = int(input("Enter number c: "))

natural_numbers.append(c)

for i in range(len(natural_numbers)-1, k, -1):
    natural_numbers[i], natural_numbers[i-1] = natural_numbers[i-1], natural_numbers[i]

natural_numbers.append(random.randrange(0, 100))

print(natural_numbers)
