print("20211127 이건호")

print("append()전용함수")
worda = []
worda.append('Seoul')
worda.append('Korea')
print(worda)

print("insert()전용함수")
wordb = ['Seoul','Korea']
wordb.insert(0,'Hi')
print(wordb)

print("extend()전용함수")
wordb = ['Seoul','Korea']
wordc = ['!']
wordb.extend(wordc)
print(wordb)

print("len() 기본함수")
print(len(wordb))
