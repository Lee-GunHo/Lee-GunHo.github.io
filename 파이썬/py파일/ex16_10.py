print("20211127 이건호")

class Exam(object):
    def __init__(self):
        self.__score = 0
    def set_score(self, score):
        self.__score = score
    def get_score(self):
        return self.__score

class Student(object):
    def __init__(self, name, totsubject):
        self.__name = name
        self.__totsubject = totsubject
        self._exam = list(range(totsubject))
        for i in range (0, totsubject):
            self._exam[i] = Exam()

def main():
    stud = Student("홍길동", 2)
    stud._exam[0].set_score(80)
    stud._exam[1].set_score(90)
    print(stud._exam[0].get_score())
    print(stud._exam[1].get_score())

if __name__ == "__main__":
    main()
    input()