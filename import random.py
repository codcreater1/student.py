import random 

class Exam():
    def __init__(self, name, subject, point):
        self.name = name
        self.subject = subject
        self.point = point
    def point_pass(self, note_student):
        passing_point = self.point + 50  
        if note_student.point >= passing_point:
            print(f"{note_student.name} passed the exam {self.subject} with {note_student.point} points.")
        elif self.point <= note_student.point:
            print(f"{note_student.name} passed the exam {self.subject} with {note_student.point} points.")
        else:
            print(f"{note_student.name} couldn't pass the exam {self.subject} with {note_student.point} points.")


student_name = input("Enter student's name: ")
student_point = int(input("Enter student's point: "))
exam_point = random.randint(0, 100)
student_1 = Exam("murat", "oop", exam_point)

student_2 = Exam(student_name, "oop", student_point)

student_1.point_pass(student_2)
