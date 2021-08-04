number: int = int(input("Input number from 3 to 9: "))

if number < 3 or number > 9:
    print("Number must be from 3 to 9!")
    exit(-1)

for i in range(1, number+1):
    palindrome_left_half: list = []
    for j in range(1, i+1):
        palindrome_left_half.append(j)

    palindrome: list = palindrome_left_half + palindrome_left_half[-2::-1]

    print(*palindrome, sep="")
