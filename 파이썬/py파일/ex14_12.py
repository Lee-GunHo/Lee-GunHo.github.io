print("20211127 이건호")

dict1 = {'title':'홍길동전',
         'author':'허균',
         'country':'한국',
         'gonre':'무협소설'}
dict2 = {'title':'춘향전',
         'author':'미상',
         'country':'한국',
         'gonre':'연애소설'}
dict3 = {'title':'놀부전',
         'author':'미상',
         'country':'한국',
         'gonre':'가족소설'}
book_list = [dict1,dict2,dict3]
for book in book_list:
    if book['country'] == '한국':
        print(f"도서명={book['title']}")
        print(book['title'])