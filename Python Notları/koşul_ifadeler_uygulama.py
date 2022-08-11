'''
ad = input('adınızı giriniz: ')
yas = int(input('yasınızı giriniz: '))

if yas >= 18:
    egitim = input('egitim bilgilerini giriniz: ')
    if egitim == 'lise' or egitim == 'üniversite':
        print(f"{ad} kişi ehliyet almaya hak kazanmıştır")
    else:
        print('egitim durumunuz uyuşmuyor')
else:
    print('yaşınız uyuşmuyor')
'''  
'''       
yazili1 = int(input('birinci yazılı notunu giriniz: '))
yazili2 = int(input('ikinci yazılı notunu giriniz: '))

sozlu = int(input('sözlü notunu giriniz: '))

ortalama = round((yazili1+yazili2+sozlu)/3)

if ortalama >= 0 and ortalama <= 24:
    print('0')
elif ortalama >= 25 and ortalama <= 44:
    print('1')
elif ortalama >= 45 and ortalama <= 54:
    print('2')
elif ortalama >= 55 and ortalama <= 69:
    print('3')
elif ortalama >= 70 and ortalama <= 84:
    print('4')
elif ortalama >= 85 and ortalama <= 100:
    print('5')
    
'''  
import datetime
tarih = input('aracını hangi tarihte trafiğe çıktı (2019.8.9): ')
tarih = tarih.split('/')
trafigeCikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
simdi = datetime.datetime.now()
fark = simdi - trafigeCikis
days = fark.days

if days<=365:
    print('1. servis aralığı')
elif days>365 and days<=365*2:
    print('2. servis aralığı')
elif days>365*2 and days<= 365*3:
    print('3. servis aralığı')
else:
    print('hatalı süre')


    
    
    
    
    
    
    
    
    
    