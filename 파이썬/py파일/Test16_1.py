print("20211127 이건호")

class Studentx(object):
    def __init__(self, name, gpa):
        self.__name = name
        self.__gpa = gpa
    @property
    def gpa(self):
        return self.__gpa
    @gpa.setter
    def gpa(self, gpa):
        self.__gpa = gpa
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name

def main():
    stud1 = Studentx("홍길동","3.5")
    print("생성 학생1",stud1.name,stud1.gpa)
    stud1.name = "성춘향"
    stud1.gpa = "4.0"
    print("변경 학생1",stud1.name,stud1.gpa)

if __name__ == "__main__":
    main()
    input()