print("20211127 이건호")

menu1 = ['라면','쫄면']
menu2 = ['만두','짬뽕']
menu = menu1 +menu2
print(menu)
menu.insert(2,'짜장면')
print(menu)
menu[2] = '짜장면'
del menu[3]
print(menu)
menu.sort()