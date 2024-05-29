print("20211127 이건호")

def addx(x,*y):
    print(y)
    total = x
    for num in y:
        total = total + num
    return total
def main():
    result1 = addx(10,2,3)
    print(result1)
    result2 = addx(10,2,3,4)
    print(result2)    

if __name__=="__main__":

    main()
    input()