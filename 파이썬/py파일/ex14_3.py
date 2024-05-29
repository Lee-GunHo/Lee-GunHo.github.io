print("20211127 이건호")

print ("while")
b= 0 
while b < 10:
    b=b+1
    if b %2 ==0: continue
    print(f"b값 = {b}")

print("for")
for c in range(1,11,2):
    if c%2 == 0: continue
    print(c)