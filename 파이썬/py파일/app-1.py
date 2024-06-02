class Student(object):
    def __init__(self,name,studnumber):
        self.__name = name
        self.__studnumber = studnumber
    def set_name(self,name):
        self.__name=name
    def get_name(self):
        return self.__name
    def set_studnumber(self,studnumber):
        self.__studnumber=studnumber
    def get_studnumber(self):
        return self.__studnumber
    def tostring(self):
        return "학번="+self.get_studnumber()+",학생이름="+self.get_name()
    
def main():
    stud1 = Student("홍길동","20XX0001")
    print(stud1.get_name())
    print(stud1.get_name(),stud1.get_studnumber())
    print(stud1.tostring())


if __name__=="__main__":

    main()
    input()