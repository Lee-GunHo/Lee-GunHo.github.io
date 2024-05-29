print("20211127 이건호")

class Student:
  def __init__(self,*args):
    self._studno = args[0]
    self._name = args[1]
    self._age = args[2]

  def info(self):
    print(f"학번 : {self._studno}")
    print("이름 : %s" %self._name)
    print("나이 : %d" %self._age)

def main():
 stud1 = Student(*["20XX01","홍길동",20])#리스트 가변인자
 #stud1 = Student(*()"20XX01","홍길동",20)) #튜플가변인자
 stud1.info()

if __name__ == "__main__":
    main()
    input()