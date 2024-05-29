print("20211127 이건호")

class Exam(object):
  def __init__(self):
     self.__subject = None
     self.__score =0
  def set_subject(self,subject):
     self.__subject = subject
  def get_subject(self):
     return self.__subject
  def set_score(self,score):
    self.__score=score
  def get_score(self):
     return self.__score
  

class Student(object):
  def __init__(self,studno,name,totsubject):
      self.__studno = studno
      self.__name = name
      self.__totsubject = totsubject
      self._exam = list(range(totsubject))
      for i in range(0,totsubject):
         self._exam[i] = Exam()
  def set_studno(self,studno):
     self.__studno =studno
  def get_studno(self):
     return self.__studno
 
  def set_name(self,name):
     self.__name =name
  def get_name(self):
     return self.__name
 
  def set_totsubject(self,totsubject):
     self.__totsubject =totsubject
  def get_totsubject(self):
     return self.__totsubject
  





  def get_gpa(self):
      _sum =0
      for i in range(0,len(self._exam)):
        _sum=_sum+self._exam[i].get_score()
      return _sum
  def get_print(self):
   print(self.get_studno(),self.get_name())
   for i in range(0,len(self._exam)):
       print(self._exam[i].get_subject(),self._exam[i].get_score())



def main():
  stud1 = Student("202301","홍길동",2)
  #print(std1._exam[0])
  stud1._exam[0].set_subject("자바")
  stud1._exam[0].set_score(80)
  stud1._exam[1].set_subject("영어")
  stud1._exam[1].set_score(90)
  stud1.get_print()
  print(stud1.get_gpa())


                       
if __name__ == "__main__":
    main()
    input()