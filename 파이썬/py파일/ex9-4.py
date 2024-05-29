print("20211127 이건호")

print ( "del a[b]인덱스 b 삭제 함수" )
wordd = ['Seoul','Korea']
del wordd[0]
print(wordd)

print("remove() 처음항목 삭제 전용함수")
worde = ['Seoul','Korea','Seoul']
worde.remove("Seoul")
print(worde)

print("max() min() 최대값 최소값 전용함수")

values = [1,3,2,5,4]
print(max(values))
print(min(values))

print("sort()전용함수")
values = [1,3,2,5,4]
values.sort()
print(values)
values.sort(reverse =True)
print(values)
wordf = ['Seoul','Deajeon','Busan']
wordf.sort()
print(wordf)