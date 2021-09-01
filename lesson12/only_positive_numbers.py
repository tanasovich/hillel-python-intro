class NegativeNumberException(Exception):
    """
    Exception, raised when negative numbers used.
    It has optional message attribute for the
    convenient problem describing.
    """
    message = "Trying to use negative numbers! Only positive allowed."

    def __init__(self, message=None):
        if message:
            self.message = message

    def __str__(self):
        return self.message


if __name__ == "__main__":
    try:
        x = int(input("Please, enter your age: "))
        if x < 0:
            raise NegativeNumberException()
    except NegativeNumberException as e:
        print(e)
        exit(-1)
    else:
        print(f"You are {x} years old.")
