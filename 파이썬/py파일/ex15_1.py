print("20211127 이건호")

dir()
dir(__builtins__)

help(dir)
help(print)

type(3.14)
type("3.14")

id(3.14)
id("3.14")

origx = [3,2,4,5,1]
sum(origx)

origx = ["seoul","deajeon","busan","inchon"]
sort_origx = sorted(origx)
print(sort_origx)

len_sort_origx = sorted(origx,key=len)
print(len_sort_origx)

reverse_len_sort_origx = sorted(len_sort_origx,reverse = True)
print(reverse_len_sort_origx)