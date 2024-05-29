print("20211127 이건호")

print("전역변수와로컬변수")
def var_test():
    b = 3
    print("로컬b= {}".format(b))
b=0
var_test()
print("글로벌 b={}".format(b))

print("로컬변수를 전역화,함수내 글로벌 변수 사용")
c = 10
def var_test2():
    global b
    b=3
    global c
    c = c+1
b=0
print(b)
var_test2()
print(b)
print(c)