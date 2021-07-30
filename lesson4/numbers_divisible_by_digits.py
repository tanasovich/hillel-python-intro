n: int = int(input("Write natural number: "))

divisible_numbers: list = []

for i in range(1, n + 1):
    for digit in str(i):
        if digit == '0' or i % int(digit) != 0:
            break
    else:
        divisible_numbers.append(i)

print(' '.join(map(str, divisible_numbers)))
