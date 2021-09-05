"""
Read text from stdin and write to the file.
Repeat action until user enters empty string.
"""
if __name__ == "__main__":
    with open("output.txt", mode="w", encoding="UTF-8") as file:
        while True:
            line = input("Please, enter text (empty string to finish input): ")
            if not line:
                break

            file.write(line + "\n")
