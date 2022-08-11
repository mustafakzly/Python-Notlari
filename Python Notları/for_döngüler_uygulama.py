'''
sayilar = [1,3,5,7,9,12,19,21]
toplam = 0
'''
'''
for a in sayilar:
    if a%3 ==0:
        print(f"{a} 3ün katlarıdır")
'''
'''
for a in sayilar:
     toplam +=a
print(toplam)
'''
'''
for a in sayilar:
    if a%2 == 0:
        print('')
    else:
        print(a**2,'tek sayıların karesi')
'''
'''
sehirler = ['kocaeli','istanbul','ankara','izmir','rize']

for a in sehirler:
    if len(a) >= 5:
        print(a)
'''
'''
urunler = [
    {'name':'samnsung s6','price':'3000'},  
    {'name':'samnsung s7','price':'4000'},
    {'name':'samnsung s8','price':'5000'},
    {'name':'samnsung s9','price':'6000'},
    {'name':'samnsung s10','price':'7000'}
]
'''
'''
toplam = 0
for a in urunler:
   fiyat = int(a['price'])
   toplam +=fiyat
print(toplam)        
'''
'''
for a in urunler:
    fiyat = int(a['price'])
    if fiyat>=5000:
        print(a)
'''