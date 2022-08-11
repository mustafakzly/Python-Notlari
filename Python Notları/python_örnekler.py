# hesap makinesi yapımı
'''
x = int(input('Birinci sayıyı giriniz: '))
y = int(input('İkinci sayıyı giriniz: '))

islem = int(input('bir işlem giriniz: '))

if islem == 1:
   print("Sonuç: ",int(x+y))
elif islem == 2:
   print("Sonuç: ",int(x*y))
elif islem == 3:
   print("Sonuç: ",int(x-y))
elif islem == 4:
   print("Sonuç: ", (x/y))
'''
#Üçgen alan hesaplama

yukseklik = int(input('yukseklik giriniz : '))
taban = int(input('taban uzunluğu giriniz : '))
kenar1 = int(input('Kenar uzunluğu giriniz : '))
kenar2 = int(input('Kenar uzunluğu giriniz : '))

alanHesapla = (yukseklik*taban)/2
cevre = (kenar1+kenar2+taban)
print('üçgenin alanı = ' , alanHesapla)
print('üçgenin cevre = ' , cevre)