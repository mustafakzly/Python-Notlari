'''
sayilar = [1,3,5,7,9,12,19,21]

i = 0
while (i< len(sayilar)):
    print(sayilar[i])
    i += 1
'''
'''
baslangic = int(input('başlangıç: '))
bitis = int(input('bitis: '))
i = baslangic
while i < bitis:
    i +=1
    if i % 2 == 1:  
        print(i)
'''
'''
i = 100

while i>0:
    print(i)
    i-=1
'''
'''
numbers = []

i = 0

while i<5:
    sayi = int(input('sayı: '))
    numbers.append(sayi)
    i+=1
numbers.sort()
print(numbers)
'''
'''
urunler = []

adet = int(input('kaç adet ürün girilecek: '))
i=0
while(i<adet):
    name = input('ürün ismi: ')
    price = input('ürün fiyatı: ')
    urunler.append({
         'name':name,
         'price':price
    })
    i+=1
for urun in urunler:
    print(f"ürün adı: {urun['name']} ürün fiyatı {urun['price']}")
'''