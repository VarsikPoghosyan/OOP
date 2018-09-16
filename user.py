class User:
    def __init__(self,first_name, last_name, ID, password, user_name, mail):
        self.first_name = first_name
        self.last_name = last_name
        self.ID = ID
        self.password = password
        self.user_name = user_name
        self.mail = mail

    def set_first_name(self):
        return self.first_name

    def get_first_name(self):
        return self.first_name

    def set_last_name(self):
        return  self.last_name

    def get_last_name(self):
        return self.last_name

    def set_ID(self):
        return self.ID

    def get_ID(self):
        return self.ID

    def set_password(self):
        return self.password

    def get_password(self):
        return self.password

    def set_user_name(self):
        return self.user_name

    def get_user_name(self):
        return self.user_name

    def set_mail(self):
        return self.mail


class Student(User):
    def __init__(self,first_name, last_name, ID, password, user_name, mail):
        User.__init__(self,first_name, last_name, ID, password, user_name, mail)
        self.courses = []
        self.assignment = []

    def set_courses(self):
        return self.courses

    def get_courses(self):
        return self.courses

    def set_assignment(self):
        return self.assignment

    def get_assignment(self):
        return self.assignment

    def displayGrades(self):
        for grade in self.displayGrades():
            print grade.course.name + ": " + grade.assignment.name + ": " + str(grade.grade.mark)


class Lecturer(User):
    def __init__(self,first_name, last_name, ID, password, user_name, mail):
        User.__init__(self,first_name, last_name, ID, password, user_name, mail)


class Grade:
    __min__ = 0
    __max__ = 100

    def __init__(self, grade):
        self.grade = grade

    def set_grade(self):
        return self.grade

    def get_grade(self):
        return self.grade


class Course:

    def __init__(self, name, ID, credit, assignment, lecturer):
        self.name = name
        self.ID = ID
        self.credit = credit
        self.assignment = assignment
        self.lecturer = lecturer

    def set_name(self):
        return self.name

    def get_name(self):
        return self.name

    def set_ID(self):
        return self.ID

    def get_ID(self):
        return self.ID

    def set_credit(self):
        return self.credit

    def get_credit(self):
        return self.credit

    def set_assignment(self):
        return self.assignment

    def get_assignment(self):
        return self.assignment

    def set_lecturer(self):
        return self.lecturer


class Assignment:

    def __init__(self, name, text, rate, deadline):
        self.name = name
        self.text = text
        self.rate = rate
        self.deadline = deadline

    def set_name(self):
         return self.name

    def get_name(self):
        return self.name

    def set_text(self):
        return self.text

    def get_text(self):
        return self.text

    def set_rate(self):
        return self.rate

    def get_rate(self):
        return self.rate

    def set_deadline(self):
        return self.deadline



class AssignmentGrade:

    def __init__(self, course, assignment, grade):
        self.course = course
        self.assignment = assignment
        self.grade = Grade(grade)
        self.state = 0

    def set_course(self):
        return self.course

    def get_course(self):
        return self.course

    def set_grade(self):
        return self.grade

    def get_grade(self):
        return self.grade


    def set_assignment(self):
        return self.assignment

    def get_assignment(self):
        return self.assignment



def main():
    course1= Course("Data Structure","ENGS115","4","python.oop","Satenik")

    assignment1 = Assignment("Assignment1", "Assign1Text", "20", "2018-09-03")
    course1.assignment.append(assignment1)

    assignment2 = Assignment("Assignment2","Assigtext2","20","2018-09-09")
    course1.assignment.append(assignment2)

    assignment3 = Assignment("Assignment3","Assigtext3","20","2018-09-16")
    course1.assignment.append(assignment3)

    student1= Student("Varsik","Poghosyan","AUA124566","AUA151516","Varsik_Poghosyan", "varsik_poghosyan@edu.aua.am")
    student1.courses.append(course1)

    assignmentgrade1=AssignmentGrade(course1,assignment1,30)
    student1.courses.append(assignmentgrade1)

    assignmentgrade2=AssignmentGrade(course1,assignment2,40)
    student1.courses.append(assignmentgrade2)

    assignmentgrade3=AssignmentGrade(course1,assignment3,50)
    student1.courses.append(assignmentgrade3)

    student1.displayGrades(),


    assignment1.name = "python.oop"
    student1.displayGrades()

    assignment2.name = "python.oop2"
    student1.displayGrades()

    assignment3.name = "python.oop3"
    student1.displayGrades()














