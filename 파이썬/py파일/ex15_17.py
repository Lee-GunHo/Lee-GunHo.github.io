print("20211127 이건호")

print("기본값 인자")
def info(name, gender=1):
    if gender == 0:
        genderx = "여자"
    else:
        genderx = "남자"
    return name, gender

def main():
    b = info("홍길동")
    c = info("성춘향",0)
    print(b)
    print(c)

if __name__=="__main__":
    main()
    input()