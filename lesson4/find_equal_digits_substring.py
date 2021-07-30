natural_number: str = input("Write natural number: ")

for digit in range(0, 10):
    if natural_number.find(str(digit) * 2) != -1:
        print("Natural number has two equal digits substring.")
        break
else:
    print("Natural number has not two equal digits substring.")
