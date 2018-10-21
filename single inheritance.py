class student:
    def ipt(self):
        student.roll=int(input("enter roll number"))
        student.name=input("enter student name")
        student.percentage=int(input("enter percentage"))
class show(student):
    def shw(self):
        print(student.__dict__)


s = show()
s.ipt()
s.shw()
