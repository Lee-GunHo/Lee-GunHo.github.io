print("20211127 이건호")

def add1(x,y):
    return x+y

add2 = lambda x,y:x+y

def main():
    print("일반 함수 이용")
    result1 = add1(2,3)
    print(result1)
    print("람다 함수 이용 1")
    result2 = add2(2,3)
    print(result2)
    print("람다 함수 이용 2")
    print( (lambda x,y:x+y)(2,3))

if __name__=="__main__":

    main()
    input()