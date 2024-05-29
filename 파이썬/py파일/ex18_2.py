print("20211127 이건호")

class AgeException(Exception):
   def __init__(self,msg):
      self.__message = msg
   
def input_age():
   age = int(input("나이 입력 : "))
   if age < 0 :
      raise AgeException("나이는 음수가 안됨")
   elif age > 150:
      raise AgeException("150살 이상 입력함")
   else:
      return age
   
def main():
   try:
      age = input_age()
   except AgeException as e:
      print(e.args[0])
   else:
      print("입력 나이는 %d 세 입니다." % age)


if __name__ =="__main__": 
   main()
   input()
