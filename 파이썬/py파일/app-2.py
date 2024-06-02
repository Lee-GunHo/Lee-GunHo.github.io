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
class Book(object):
    def __init__(self,isbn,title,author,student):
        self.__isbn=isbn
        self.__title=title
        self.__author =author
        self._student = student
    
    def set_isbn(self,isbn):
        self.__isbn=isbn
    def get_isbn(self):
        return self.__isbn
    
    def set_title(self,title):
        self.__title=title
    def get_title(self):
        return self.__title
    
    def set_author(self,author):
        self.__author=author
    def get_author(self):
        return self.__author
    
    def set_student(self,student):
        self._student=student
    def get_student(self):
        return self._student
    def tostring(self):
        available = "대출가능"
        if(self.get_student() ==None):
            available = "대출가능"
        else:
            available= "대출자="+self.get_student().get_name()
        return "ISBN="+self.get_isbn()+",제목 = "+self.get_title()+"저자="+self.get_author()+","+available

def main():
    stud1 = Student("홍길동","20XX0001")
    print(stud1.tostring())
    book1 = Book("000101","홍길동전","허균",None)
    print(book1.tostring())
    book2 = Book("000102","춘향전","미상",stud1)
    print(book2.tostring())


if __name__=="__main__":

    main()
    input()