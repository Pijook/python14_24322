class Student:
    def __init__(self, mail, name, surname, points):
        self.mail = mail
        self.name = name
        self.surname = surname
        self.points = points
        self.graded = None
        self.mailed = None


students = {}

file_name = "ppy.txt"
file = open(file_name, "r")

for line in file:
    parts = line.split(" ")

    temp_student = Student(parts[0], parts[1], parts[2], parts[3])

    if len(parts) >= 5:
        temp_student.graded = parts[4]
    if len(parts) >= 6:
        temp_student.mailed = parts[5]

    students[temp_student.mail] = temp_student
