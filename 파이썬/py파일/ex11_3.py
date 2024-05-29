print("20211127 이건호")

print("#dictionary 삭제")
tv = {'TV55':100, 'TV65':150, 'TV75':200}
del tv['TV65']
print(tv)

print("#dictionary keys()")
tv = {'TV55':100,'TV75':200}
keys = tv.keys()
print(keys)

print("#dictionary values()")
tv = {'TV55':100,'TV75':200}
values = tv.values()
print(values)

print("#dictionary items()")
tv = {'TV55':100,'TV75':200}
items = tv.items()
print(items)
