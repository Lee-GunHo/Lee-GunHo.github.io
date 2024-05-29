print("20211127 이건호")

print("키워드 가변인자")

def addz(num1, *data_list, **dict):
    for key in dict:
        print(key, ":", dict[key])
    sum = num1
    for x in data_list:
        sum = sum + x
    return sum

def main():
    b = addz(1,2,3,4,5, start="1",end="5")
    print(b)
    c = addz(1,2,3,3,4,5,6,7,8,9,10,start = "1", end="10")
    print(c)

if __name__=="__main__":
    main()
    input()
    