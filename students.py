class student:
    def __init__(self, name, klass, grade):
        self.name=name
        self.grade=grade

    def add_grade(self, subject, grade):
        self.grade[subject].append(grade)
        return self.grade
    def average(self, grades):
        self.grades = grades
    def calculate_average(self):
        return
I = student(
    name = 'I',
        grades ={
            'математика':[2, 3, 4, 5]
        }
    )
