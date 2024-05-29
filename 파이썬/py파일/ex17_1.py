print("20211127 이건호")

class Animal1(object):
   def __init__(self,name):
      self.__name =name
   @property
   def name(self):
      return self.__name
   @name.setter
   def name(self,name):
      self.__name = name
   def print_info(self):
      print(f"슈퍼 클래스 사용, 이름: {self.name}")
      #self.__name동일
class Cat1(Animal1):
   pass
def main():
   my_cat = Cat1("고양이")
   my_cat.print_info()

if __name__ =="__main__": 
   main()
   input()
