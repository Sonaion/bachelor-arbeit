class Student:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def __repr__(self):
        return str(self.name)


def function(student_array):
    return [student for student in student_array if student.age >= 18]


students = []
students.append(Student(17, "Hans"))
students.append(Student(21, "Jasmin"))
students.append(Student(32, "Florian"))
print(function(students))
