print("20211127 이건호")

def sumx(num):
    if num == 1:
        return 1
    else :
        return sumx(num-1)+num
    
def main():
    b = sumx(5)
    print(b)
    c = sumx(10)
    print(c)

if __name__=="__main__":

    main()
    input()
    