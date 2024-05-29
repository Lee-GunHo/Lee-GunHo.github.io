print("20211127 이건호")

def addx(num1,num2):
    c=num1+num2
    return num1,num2,c


def main():
    input1,input2,sum = addx(10,20)
    print("다수 결과값 각각 반환")
    print(input1,input2,sum)

    print("다수 결과값 튜플로 반환")
    result = addx(30,40)
    print(result)
    print(result[0])
    print(result[1])
    print(result[2])

if __name__=="__main__":

    main()
    input()