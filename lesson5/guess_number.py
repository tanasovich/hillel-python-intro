import random


guessed_number: int = random.randint(1, 100)
number_of_attempts: int = 0

while True:
    answer = input("Guess number from 1 to 100: ")
    number_of_attempts += 1

    if not answer.isdecimal():
        print("This is not a decimal number!")
        continue

    number: int = int(answer)

    if number < 1 or number > 100:
        print("Number must be from 1 to 100!")
    elif number < guessed_number:
        print("Number is less than guessed number.")
    elif number > guessed_number:
        print("Number is greater than guessed number.")
    else:
        print(f"You guessed the number {guessed_number} to the {number_of_attempts} attempt")
        break
