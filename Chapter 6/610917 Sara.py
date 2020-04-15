class StudentName:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def __str__(self):
        return (self.firstname + " " + self.lastname)

    def getFirstName(self):
        return self.firstname

    def getLastName(self):
        return self.lastname

    def setFirstName(self, firstname):
        self.firstname = firstname

    def setLastName(self, lastname):
        self.lastname = lastname

    def getStudentName(self):
        return (self.firstname + " " + self.lastname)

class StudentScore:
    def __init__(self, score):
        self.score = score

    def __str__(self):
        return self.score

    def getScore(self):
        return self.score

    def setScore(self, score):
        self.score = score

class StudentsDataException(Exception):
    pass

class BadLine(StudentsDataException):
    pass

class FileEmpty(StudentsDataException):
    pass

jekyll_file = input("Enter Prof. Jekyll's file name: ")
open_jekyll_file = open(jekyll_file)
jekyll_contents = open_jekyll_file.readlines()
open_jekyll_file.close()

if len(jekyll_contents) == 0:
    raise FileEmpty("File is empty.")

studentDict = {}

for s in jekyll_contents:
    sli = s.rstrip("\n").split(sep="\t")
    
    if len(sli) != 3:
        raise BadLine("Input error.")
    if type(sli[0]) and type(sli[1]) != str:
        raise BadLine("Input error.")
    if type(float(sli[2])) == str:
        raise BadLine("Input error.")
    
    name = StudentName(sli[0], sli[1])
    score = StudentScore(float(sli[2]))
    if name.getStudentName() not in studentDict:
        studentDict[name.getStudentName()] = score.getScore()
    else:
        studentDict[name.getStudentName()] = studentDict[name.getStudentName()] + score.getScore()

for key in sorted(studentDict):
    print(key, studentDict[key])
