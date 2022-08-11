message = 'Hello world. Mustafa KIZILAY'

#message = message.upper() # bütün karakterler büyük 
#message = message.lower() # bütün karakterler küçük
#message = message.title() # baş harfler büyük olur
#message = message.capitalize() # sadece ilk harf büyük olur
#message = message.strip() #baştaki boşluk gider
#message = message.split() # her bir kelimeye ayrı ayrı ulaşılabilir dizi gibi
#message = message.split('.') # . dan sonra ve önce olarak diziye ayırır
#message = '#'.join(message) # tek yazılırsa her araya # ekler
#message = message.find('KIZILAY')
#isFound = message.startswith('H')
#isFound = message.endswith('Y')
#print(message)
#print(isFound)

#message = message.replace('Mustafa', 'Hüseyin') # yer değiştirme
message = message.center(50,'-')
print(message)