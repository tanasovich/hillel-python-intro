EXPECTED_PASSWORD = "I wanna be like Kevin"

actual_password: str = input("Please, write a password: ")

print("Password is valid." if actual_password == EXPECTED_PASSWORD else "Password is not valid!")
