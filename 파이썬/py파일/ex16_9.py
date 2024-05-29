print("20211127 이건호")

class Studentx(object):
    def __init__(self, num, name, gpa):
        self.__num = num
        self.__name = name
        self.__gpa = gpa
    def get_num(self):
        return self.__num
    def set_num(self, num):
        self.__num = num
    def get_gpa(self):
        return self.__gpa
    def set_gpa(self, gpa):
        self.__gpa = gpa
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name

def main():
    stud1 = Studentx("20211127","홍길동","3.5")
    print("생성 학생1",stud1.get_num(),stud1.get_name(),stud1.get_gpa())
    stud1.set_num("20211128")
    stud1.set_name("성춘향")
    stud1.set_gpa("4.0")

    print("변경 학생1",stud1.get_num(),stud1.get_name(),stud1.get_gpa())

if __name__ == "__main__":
    main()
    input()