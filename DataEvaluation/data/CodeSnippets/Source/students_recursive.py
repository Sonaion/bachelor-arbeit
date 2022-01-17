class Student:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def __repr__(self):
        return str(self.name)


def function(student_array):
    if len(student_array) == 0:
        return []
    elif student_array[0].age >= 18:
        return [student_array[0]] + function(student_array[1:])
    else:
        return function(student_array[1:])


students = []
students.append(Student(17, "Hans"))
students.append(Student(21, "Jasmin"))
students.append(Student(32, "Florian"))
print(function(students))
