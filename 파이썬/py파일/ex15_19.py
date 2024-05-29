print("20211127 이건호")

def addz(num1, *data_list):
    sum = num1
    for x in data_list:
        sum = sum + x
    return sum

def main():
    b=addz(1,2,3,4,5)
    print(b)
    c=addz(1,2,3,4,5,6,7,8,9,10)
    print(c)

if __name__=="__main__":
    main()
    input()

