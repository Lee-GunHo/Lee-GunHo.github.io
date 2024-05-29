print("20211127 이건호")

class Exam(object):
    def __init__(self):
        self.__score = 0
    def set_score(self, score):
        self.__score = score
    def get_score(self):
        return self.__score

class Student(object):
    def __init__(self, name):
        self.__name = name
        self.__exam = Exam()
    def get_name(self):
        return self.__name
    def get_exam(self):
        return self.__exam
    def set_exam(self,value):
        self.__exam.set_score(value)

def main():
    stud1 = Student("홍길동")
    stud1.set_exam(80)
    print(stud1.get_name(), stud1.get_exam().get_score())
if __name__ == "__main__":
    main()
    input()    