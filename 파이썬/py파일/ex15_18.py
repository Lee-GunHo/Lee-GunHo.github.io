print("20211127 이건호")

print("키워드입력")
def info(name,gender):
    if gender == 0:
        genderx = "여자"
    else:
        genderx = "남자"
    return name, gender

def main():
    b=info(gender=1,name="홍길동")
    c=info("성춘향", gender=0)
    print(b)
    print(c)

if __name__=="__main__":
    main()
    input()