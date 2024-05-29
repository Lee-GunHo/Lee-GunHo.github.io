print("20211127 이건호")

tv = {'TV55':100, 'TV65':150, 'TV75':200}
print ("# dictionary key 인쇄")
for key in tv:
    print(key)
print("#tv.key()이용key 인쇄")
for key in tv.keys():
    print(key)
print("#tv.key()이용 value 인쇄")
for value in tv.values():
    print(value)
print("#tv.key()이용 key,value 인쇄")
for key,value in tv.items():
    print(key,value)


