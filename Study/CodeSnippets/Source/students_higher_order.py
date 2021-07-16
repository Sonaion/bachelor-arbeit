class Student:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def __repr__(self):
        return str(self.name)


def function(student_array):
    return list(filter(lambda x: x.age >= 18, student_array))


students = []
students.append(Student(17, "Hans"))
students.append(Student(21, "Jasmin"))
students.append(Student(32, "Florian"))
print(function(students))
