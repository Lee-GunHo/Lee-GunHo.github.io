menu = 0
food = []

while menu != 5:
    print("-"*10)
    print("""
    1.보관 식재료 출력
    2.식재료 추가
    3.식재료 삭제
    4.식재료 변경
    5. 종료""")
    print("-"*10)
    menu = int(input("관리 메뉴를 선택하시오:"))
    if menu == 1:
        print(food)
    elif menu == 2:
        name = input("추가할 식재료를 입력하시오:")
        food.append(name)
        print(food)
    elif menu == 3:
        eli_name = input("삭제할 식재료를 입력하시오:")
        if eli_name in food:
            food.remove(eli_name)
        else:
            print("식재료 재고 없음")
    elif menu == 4:
        exch_name = input("교환할 식재료를 입력하시오:")
        if exch_name in food:
            idx = food.index(exch_name)
            new_name = input("새로운 식재료를 입력하시오:")
            food[idx] = new_name
        else:
            print("식재료 재고 없음")
    elif menu == 5:
        print("종료합니다.")
        break