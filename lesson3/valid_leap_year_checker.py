year: int = int(input("Enter a year: "))

if year < 1900 or year > 1000000:
    print("Year is not valid!")
    exit(-1)

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            is_leap_year = True
        else:
            is_leap_year = False
    else:
        is_leap_year = True
else:
    is_leap_year = False

print(f"{year} is a leap year" if is_leap_year else f"{year} is not a leap year")
