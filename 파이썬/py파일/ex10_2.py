print("20211127 이건호")

print("#tuple 인덱싱")
tuplea = ( 1,2,'love','korea')
print(tuplea[2])
print(tuplea[-1])

print("#리스트 변환을 통한 tuple 수정")
tupleb = ( 1,2,'love','korea')
tupleb = list(tupleb)
tupleb[2] = 'like'
tupleb = tuple(tupleb)
print(tupleb[2])

print("#tuple 슬라이싱")
tuplec = ( 1,2,'love','korea')
new = tuplec[1:3]
print(new)
