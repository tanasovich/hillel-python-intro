numbers: list = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
power = input("Enter power (by default it equals 2): ")

power_lambda = lambda x, y=2: x**y

powered_numbers: map = None

if power == '':
    powered_numbers = map(power_lambda, numbers)
else:
    power = int(power)
    powered_numbers = map(power_lambda, numbers, [power]*len(numbers))

print(list(powered_numbers))
