print("20211127 이건호")

dict1 = {'한국어':'아침','영어':'Morning','독일어':'Morgen'}
dict2 = {'한국어':'점심','영어':'Afternoon','독일어':'Nachmittag'}
dict3 = {'한국어':'저녁','영어':'Evening','독일어':'Abend'}
d_list = [dict1,dict2,dict3]
for dict in d_list:
    if dict['한국어']=='아침':
     print(dict['영어'])
     print(dict['독일어'])
