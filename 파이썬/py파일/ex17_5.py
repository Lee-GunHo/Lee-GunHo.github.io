print("20211127 이건호")

class Animal3(object):
   def __init__(self,name):
      self.__name= name
   @property
   def name(self):
      return self.__name
   @name.setter
   def name(self,name):
      self._name = name
   def print_info(self):
      print(f"슈퍼 클래스 사용, 이름: {self.name}")
class Cat3(Animal3):
   def __init__(self,name,color):
      Animal3.__init__(self,name)
      #super().__init__(name)
      self.__color = color
   @property
   def color(self):
      return self.__color
   @color.setter
   def color(self,color):
      self.__color = color
   def print_color(self):
      print(f"서브 클래스 메소드 추가, 컬러: {self.color}")

def main():
   my_cat = Cat3("고양이","Red")
   my_cat.print_info()
   my_cat.print_color()

if __name__ =="__main__": 
   main()
   input()

