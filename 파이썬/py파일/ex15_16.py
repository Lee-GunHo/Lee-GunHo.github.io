print("20211127 이건호")

def info(x,**y):
    print(y)
    total = x
    for key,value in y.items():
        print(f"{key}:{value}")

    return x 
    
def main():
    dict1 = {"name":"홍길동","age":"20","city":"컴공"}
    result = info(10,**dict1)
    print(result)    

if __name__=="__main__":

    main()
    input()