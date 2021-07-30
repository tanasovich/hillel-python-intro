natural_number: str = input("Write natural number: ")

for digit in list(range(0, 10)):
    if natural_number.count(str(digit)) == 2:
        print("Natural number has two equal digits.")
        break
else:
    print("Natural number has not two equal digits.")
