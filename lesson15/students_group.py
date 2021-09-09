class Student:
    def __init__(self, name: str, age: int, grades: list[int]):
        self.name = name
        self.age = age
        self.grades = grades


class Group:
    def __init__(self, students: list[Student]):
        self.students = students

    def print_students_with_scores(self):
        pass
