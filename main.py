class grade:
    min=0
    max=100

    def __init__(self, grade):
        self.grade = grade
#classmethod
        def set_grade(self,grade):
            return self.grade

        def get_grade(self):
            return self.grade

        def check_if_valid(self, grade):
            return self.grade
class assignment:
    min=0
    max=100

    def __init__(self, name, percent, grade, deadline, status, description):
        self.name = name
        self.percent = percent
        self.grade = grade
        self.deadline = deadline
        self.status = status
        self.description = description
        
 #classmethod
        def sets(self):
            return self.name
        def gets(self):
            return gets.name
        def check_if_graded(self)
class courses:

    def __init__(self, name, ID, credit, assignement, lecturer):
        self.name = name
        self.ID = ID
        self.credit = credit
        self.assignment = assignement
        self.lecturer = lecturer




