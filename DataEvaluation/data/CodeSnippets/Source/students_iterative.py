class Student:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def __repr__(self):
        return str(self.name)


def function(student_array):
    result = []
    for student in student_array:
        if student.age >= 18:
            result.append(student)
    return result


students = []
students.append(Student(17, "Hans"))
students.append(Student(21, "Jasmin"))
students.append(Student(32, "Florian"))
print(function(students))
