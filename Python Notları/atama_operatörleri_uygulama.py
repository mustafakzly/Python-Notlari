x,y,z = 2,5,10

numbers = 1,5,7,10,6
#toplam = x+y+z

#x = int(input('ilk sayıyı giriniz : '))
#y = int(input('ikinci sayıyı giriniz : '))
#sonuc1 = x*y-toplam
#print(sonuc1)

#sonuc2 = y//x
#print(sonuc2)

#sonuc3 = toplam%3
#print(sonuc3)

#sonuc4 = y**x
#print(sonuc4)

#x,*y,z = numbers
#result = z**3
#print(result)

x,*y,z = numbers
result = y[0]+ y[1]+ y[2]
print(result)