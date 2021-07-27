a: int = int(input("Enter integer a: "))
b: int = int(input("Enter integer b: "))

a ^= b
b ^= a
a ^= b

print(f"Swapped integers a = {a} and b = {b}")
