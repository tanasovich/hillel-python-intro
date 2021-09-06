"""
Read, calculate metrics and write table.
Average grade calculating, displaying students with low grades,
beautiful table printing.
"""


def create_student(firstname: str, lastname: str, average_grade: float) -> dict:
    """
    Accepts student credits and returns populated dictionary.

    :param firstname: students firstname
    :param lastname: students lastname
    :param average_grade: average grade
    :return: dictionary with input params
    """
    return {
        'firstname': firstname,
        'lastname': lastname,
        'average_grade': average_grade
    }


def calculate_average_grade(grades: list[int]) -> float:
    """
    Accepts list with grades and computes average grade.

    :param grades: list with grades
    :return: average grade
    """
    return sum(grades) / len(grades)


def formatted_student_credits(student: dict, desired_width: int) -> str:
    """
    Accepts student credits (dictionary) and desired prompt width.
    Returns formatted text with student information.

    :param student: dictionary with student credits
    :param desired_width: desired student credits width in prompt
    :return: formatted student information
    """
    fullname = "{} {}.".format(student['lastname'], student['firstname'][0])
    formatted_grade = "{:.2f}".format(student['average_grade'])
    return fullname + formatted_grade.rjust(desired_width-len(fullname))


def print_weak_students_and_score(students: list) -> None:
    """
    Print students with less than 5 average grade.
    Calculate and print students' average grade.

    :param students: students list
    :return: None
    """
    for student in students:
        if student['average_grade'] < 5:
            print(formatted_student_credits(student, 24))

    average_grades = [student['average_grade'] for student in students]
    print("Средний балл по классу: {:.2f}".format(
        calculate_average_grade(average_grades))
    )


def read_students_from(file) -> list:
    """
    Reads student credits from file.
    Returns list composed with students' information.

    :param file: file to be read
    :return: students list
    """
    students = list()
    while True:
        line: str = file.readline()
        if not line:
            break

        firstname, lastname, *grades = line.split()
        average_grade = calculate_average_grade(list(map(int, grades)))
        students.append(create_student(firstname, lastname, average_grade))

    return students


def write_students_to(students: list, file) -> None:
    """
    Writes student credits to file.

    :param students: students list
    :param file: file to be written
    :return: None
    """
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
