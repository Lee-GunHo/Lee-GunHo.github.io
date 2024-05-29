print("20211127 이건호")


print("비트논리 연산자 결과 인쇄")
a= 11
b = 13
ba = (bin(a))
print(f"2진수 : {ba}")
bb = (bin(b))
print(f"2진수 : {bb}")
# a&b
ab = bin(a&b)
print(f"&연산 : {ab}")
print(f"&연산자 : {a&b}")
ab = bin(a|b)
print(f"&연산 : {ab}")
print(f"&연산자 : {a|b}")
ab = bin(a^b)
print(f"&연산 : {ab}")
print(f"&연산자 : {a^b}")