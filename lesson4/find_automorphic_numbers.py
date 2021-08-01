n: int = int(input("Write natural number N: "))

for number in range(1, n+1):
    squared_number = number**2
    if str(squared_number).endswith(str(number)):
        print(f"{number} * {number} = {squared_number}")
