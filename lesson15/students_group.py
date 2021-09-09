class Student:
    def __init__(self, name: str, age: int, grades: list[int]):
        self.name = name
        self.age = age
        self.grades = grades


class Group:
    def __init__(self, students: list[Student]):
        self.students = students

    def print_students_with_scores(self, desired_width: int):
        for student in self.students:
            grades = ""

            for i in range(len(student.grades)):
                grades += str(student.grades[i])
                if i < len(student.grades) - 1:
                    grades += " "

            print(student.name + grades.rjust(
                desired_width - len(student.name)))
