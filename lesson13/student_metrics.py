def populate_student(firstname: str, lastname: str, average_grade: float) -> dict:
    return {
        'firstname': firstname,
        'lastname': lastname,
        'average_grade': average_grade
    }


def calculate_average_grade(grades: list[int]) -> float:
    return sum(grades) / len(grades)


def formatted_student_credits(student: dict, desired_width: int) -> str:
    fullname = "{} {}.".format(student['lastname'], student['firstname'][0])
    formatted_grade = "{:.2f}".format(student['average_grade'])
    return fullname + formatted_grade.rjust(desired_width-len(fullname))


def print_weak_students_and_score(students: list) -> None:
    for student in students:
        if student['average_grade'] < 5:
            print(formatted_student_credits(student, 24))
    else:
        average_grades = [student['average_grade'] for student in students]
        print("Средний балл по классу: {:.2f}".format(calculate_average_grade(average_grades)))


def read_students_from(file) -> list:
    students = list()
    while True:
        line: str = file.readline()
        if not line:
            break

        firstname, lastname, *grades = line.split()
        average_grade = calculate_average_grade(list(map(int, grades)))
        students.append(populate_student(firstname, lastname, average_grade))

    return students


def write_students_to(students: list, file) -> None:
    for student in students:
        file.write(formatted_student_credits(student, 24))
        file.write("\n")


if __name__ == "__main__":
    file_to_read = open("src_14.txt", mode="r", encoding="UTF-8")
    students = read_students_from(file_to_read)
    file_to_read.close()

    print_weak_students_and_score(students)

    file_to_write = open("output.txt", mode="w", encoding="UTF-8")
    write_students_to(students, file_to_write)
    file_to_write.close()
