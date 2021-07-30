natural_number: str = input("Write natural number: ")

digits_sum: int = 0

for digit in natural_number:
    digits_sum += int(digit)

print(f"Digits sum equals to {digits_sum}")
