print("20211127 이건호")

print("#set 합집합")
set1 = set([1,2,3,4,5])
set2 = set([3,4,5,6,7])
print(set1|set2)

print("#set 교집합")
set1 = set([1,2,3,4,5])
set2 = set([3,4,5,6,7])
print(set1&set2)

print("#set 차집합")
set1 = set([1,2,3,4,5])
set2 = set([3,4,5,6,7])
print(set1-set2)
print(set2-set1)
