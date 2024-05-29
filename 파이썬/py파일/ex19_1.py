print("20211127 이건호")

# ==== 단순 메뉴 =====
def main():
   #store = Store("카페")
   choice = None
   while True:
      print("---메뉴---")
      print("1. 음료")
      print("2. 알콜")
      print("3. 영수증")
      print("4. 종료")
      choice = input("메뉴입력 :")
      if choice == "1":
         print("음료 선택함")
         product = input("이름 입력:")
         price = input("단가 입력:")
         quantity = input("갯수 입력:")
         print("{},{},{}".format(product,price,quantity))

      #beverage = Beverage(product,price,quantity)
      #print(beverage)
      #store.add_beverage(beverage)
      elif choice =="2":
         print("알콜 선택함")
         product = input("이름 입력: ")
         price = input("단가입력 :")
         quantity = input("갯수입력 :")
         alcohol = input("알콜도수 입력 :")
         print("{},{},{}".format(product,price,quantity,alcohol))
         #liquor = Liquor(product,price,quantity,alcohol)
         #store.add_liquor(liauor)
      elif choice =="3":
         print("영수증 선택함")
         #store.rpint_reciept()
      elif choice =="4":
         print("종료 선택함")
         break
      else:
         print("1~4 사이 숫자를 입력하세요")
         
if __name__ =="__main__": 
   main()
   
