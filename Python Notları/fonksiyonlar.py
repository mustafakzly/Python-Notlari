'''
def sayHello(name = 'user'):
    print('hello '+ name)
sayHello('mustafa')
sayHello()
'''

def sayHello(name = 'user'):
    return 'hello ' + name

msg = sayHello('mustafa')
print(msg)

def total(num1,num2):
    return num1 + num2
sayi = total(10,5)
print(sayi)

def yasHesapla(dogumYili):
    return 2022 - dogumYili

hesapla = yasHesapla(2000)
print(hesapla)

def Emeklilik(dogumYili, isim):
    yas = yasHesapla(dogumYili)
    emek = 65 - yas
    
    if emek > 0 :
        print(f"emekeliliğinize {emek} yıl kaldı.")
    else:
        print('zaten emekli oldunuz.')

Emeklilik(1983, 'ali')
Emeklilik(1950, 'ahmet')

