class dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def set_age(self, age):
        self.age=age
    def set_name(self, name):
        self.name = name
d=dog("Tim", 45)
d.set_age(23)
d.set_name("mande")
print(d.get_age(), d.name)




#creating students class
class student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade # grade from 0 to 100
    def get_grade(self):
        return self.grade

class course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students=max_students
        self.students = []
    def add_students(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return  True
        return False
    def get_average_grade(self):
        value=0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)
s1=student("Tim", 19, 95)
s2=student("Bill", 19, 75)
s3=student("jill", 19, 65)

course = course("Science", 2)
course.add_students(s1)
course.add_students(s2)
print(course.get_average_grade())