print("20211127 이건호")

def no_param():
    print("입력값이 없는 함수")
    return "Hello"

def no_return(num1,num2):
    print("반환값이 없는 함수")
    print(num1,num2)
    return

def main():
    b = no_param()
    print(b)
    c = no_return(3,5)
    print(c)
if __name__=="__main__":

    main()
    input()