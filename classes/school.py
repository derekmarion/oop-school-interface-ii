from classes.staff import Staff
from classes.student import Student

class School:
    def __init__(self, name):
        self.name = name
        self.staff = Staff.objects()
        self.students = Student.objects()

    def list_students(self):
        counter = 1
        for student in (self.students):
            print(f"{counter}. {student.name} {student.school_id}")
            counter += 1

    def find_student_by_id(self, student_id):
        for student in (self.students):
            if student_id == student.school_id:
                return student
        return "\nStudent not found."
