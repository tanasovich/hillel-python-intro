class Student:
    def __init__(self, name: str, age: int, grades: list[int]):
        self.name = name
        self.age = age
        self.grades = grades


class Group:
    def __init__(self, students: list[Student]):
        self.students = students

    def print_students_with_scores(self, desired_width: int = 20):
        for student in self.students:
            grades = ""

            for i in range(len(student.grades)):
                grades += str(student.grades[i])
                if i < len(student.grades) - 1:
                    grades += " "

            print(student.name + grades.rjust(
                desired_width - len(student.name)))


if __name__ == "__main__":
    student1 = Student("John", 18, [3, 3, 3, 3])
    student2 = Student("Nina", 21, [4, 5, 4, 4])
    student3 = Student("Chin", 19, [5, 5, 5, 5])
    students = [student1, student2, student3]

    group = Group(students)
    group.print_students_with_scores()
