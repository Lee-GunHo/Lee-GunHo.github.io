class Student(object):
    def __init__(self, name, studnumber):
        self.__name = name
        self.__studnumber = studnumber

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_studnumber(self, studnumber):
        self.__studnumber = studnumber

    def get_studnumber(self):
        return self.__studnumber

    def tostring(self):
        return "학번=" + self.get_studnumber() + ",학생이름=" + self.get_name()


class Book(object):
    def __init__(self, isbn, title, author, student=None):
        self.__isbn = isbn
        self.__title = title
        self.__author = author
        self.__student = student

    def set_isbn(self, isbn):
        self.__isbn = isbn

    def get_isbn(self):
        return self.__isbn

    def set_title(self, title):
        self.__title = title

    def get_title(self):
        return self.__title

    def set_author(self, author):
        self.__author = author

    def get_author(self):
        return self.__author

    def set_student(self, student):
        self.__student = student

    def get_student(self):
        return self.__student

    def tostring(self):
        student_info = "None" if self.__student is None else self.__student.get_name()
        return f"ISBN={self.get_isbn()}, 제목={self.get_title()}, 저자={self.get_author()}, 대출자={student_info}"


class Bookstore(object):
    def __init__(self, storename, books=None, students=None):
        if books is None:
            books = []
        if students is None:
            students = []
        self.__storename = storename
        self.__books = books
        self.__students = students

    def get_storename(self):
        return self.__storename

    def set_storename(self, storename):
        self.__storename = storename

    def get_students(self):
        return self.__students

    def set_students(self, students):
        self.__students = students

    def get_books(self):
        return self.__books

    def set_books(self, books):
        self.__books = books

    def add_book(self, book):
        self.__books.append(book)

    def remove_book(self, book):
        self.__books.remove(book)

    def add_student(self, student):
        self.__students.append(student)

    def remove_student(self, student):
        self.__students.remove(student)

    def checkout(self, book, student):
        if book.get_student() is None:
            book.set_student(student)
            return True
        else:
            return False

    def checkin(self, book):
        if book.get_student() is not None:
            book.set_student(None)
            return True
        else:
            return False

    # 학생별 대여도서 목록
    def get_books_for_student(self, student):
        result = []
        for abook in self.__books:
            if abook.get_student() is not None and abook.get_student().get_studnumber() == student.get_studnumber():
                result.append(abook)
        return result

    # 대출 가능 도서 목록
    def get_available_books(self):
        result = []
        for abook in self.__books:
            if abook.get_student() is None:
                result.append(abook)
        return result

    # 대출 불가능 도서 목록
    def get_unavailable_books(self):
        result = []
        for abook in self.__books:
            if abook.get_student() is not None:
                result.append(abook)
        return result

    # 도서관 보유책수 및 회원수 명세 설명
    def tostring(self):
        return self.get_storename() + ", 보유책=" + str(len(self.get_books())) + "권, 회원수=" + str(len(self.get_students())) + "명"

    # 도서관 현황 레포트
    def print_status(self):
        print("=== 도서관 현황 시작 ===")
        print(self.tostring())
        for abook in self.get_books():
            print(abook.tostring())
        for astudent in self.get_students():
            count = len(self.get_books_for_student(astudent))
            print(astudent.tostring() + "(은/는) " + str(count) + "권 대출중")
        print("대출가능책 " + str(len(self.get_available_books())) + "권")
        print("=== 도서관 현황 완료 ===")


def main():
    mystore = Bookstore("한국도서관")  # 도서관 생성
    # 학생회원 객체 생성(3명)
    stud1 = Student("이몽룡", "20XX0001")
    stud2 = Student("변학도", "20XX0002")
    stud3 = Student("심봉사", "20XX0003")
    # 도서 객체 생성(3권)
    book1 = Book("00101", "홍길동전", "허균", None)
    book2 = Book("00102", "춘향전", "미상", None)
    book3 = Book("00103", "심청전", "미상", None)
    # 학생회원을 도서관에 등록
    mystore.add_student(stud1)
    mystore.add_student(stud2)
    mystore.add_student(stud3)
    # 도서를 도서관에 등록
    mystore.add_book(book1)
    mystore.add_book(book2)
    mystore.add_book(book3)
    # 도서관 현재 상태 인쇄
    print(mystore.print_status())
    # 도서 book1 홍길동전을 stud2 변학도에게 대출
    mystore.checkout(book1, stud2)
    # 도서 book2 춘향전을 stud1 이몽룡에게 대출
    mystore.checkout(book2, stud1)
    # 도서관 현재상태 인쇄
    print(mystore.print_status())
    # 도서 book1 홍길동전 반납
    mystore.checkin(book1)
    # 도서관 현재 상태 인쇄
    print(mystore.print_status())


if __name__ == "__main__":
    main()
    input()