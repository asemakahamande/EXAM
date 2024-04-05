"""Let say you are a teacher and you have different students
records  containing id  of students and the marks list in each subject
where different students have taken diffferent number of subjects. All
records ar in hard copy. you want to enter all the data in computer and
want to compute the average marks of each student and display"""


def getDataFromUser():
    D = {}
    while True:
        studentId = input("Enter student ID:")
        marksList = input("Enter the marks by comma separated value:")
        moreStudents = input('Enter "no" to quit insertion: ')
        if studentId in D:
            print(studentId, "is already inserted")
        else:
            D[studentId] = marksList.split(",")
        if moreStudents.lower() == "no":
            return D

getDataFromUser()