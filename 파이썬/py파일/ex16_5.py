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
        self._name = name
        self._exam = Exam()
    def get_name(self):
        return self._name
def main():
    stud1 = Student("홍길동")
    stud1._exam.set_score(80)
    print(stud1.get_name(), stud1._exam.get_score())
if __name__ == "__main__":
    main()
    input()    