print("20211127 이건호")

def divide_by_zero_except(a,b):
   try:
      result = a/b
   except ZeroDivisionError:
      print("0으로 나누기 안됨")
   except:
      print("ZeroDivisionError 이외 예외 발생함")
   else:
      return result
   finally:
      print("나누기를 수행함")
   
def main():
   result = divide_by_zero_except(3,0)
   print(result)
   result = divide_by_zero_except(None,2)
   print(result)

if __name__ =="__main__": 
   main()
   input()
