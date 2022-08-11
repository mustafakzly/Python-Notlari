'''
sayi = int(input('bir sayi giriniz: '))
if sayi >= 0 and sayi <= 100:
    print('0 la 100 aralığındandır')
else:
    print('0 la 100aralığında değildir')
'''
'''
sayi = int(input('bir sayi giriniz: '))
if sayi%2 == 0 and sayi >0:
    print('sayi pozitif bir çift sayıdır')
elif sayi < 0:
    print('sayi pozitif değildir')
else:
    print('sayi çift değildir')
'''
'''
email = 'mustafa@gmail.com'
password = '1234'

Email = input('email adresinizi giriniz: ')
if email == Email:
    Password = input('passawordunuzu giriniz: ')
    if password == Password:
        print('kullanıcı girişi başarılı.')
    else:
        print('şifre yanlış')
else:
    print('email yanlış')
'''
'''
s1 = int(input('Birinci sayıyı giriniz: '))
s2 = int(input('İkinci sayıyı giriniz: '))
s3 = int(input('Üçüncü sayıyı giriniz: '))

if s1 > s2 and s1 > s3:
    print(f"{s1} aralarındaki en büyük sayı")
elif s2 > s3 and s2 > s1:
    print(f"{s2} aralarındaki en büyük sayı")
elif s3 > s1 and s3 > s2:
    print(f"{s3} aralarındaki en büyük sayı")
'''
'''
vize1 = int(input('birinci vizeyi giriniz: '))
vize2 = int(input('ikinci vizeyi giriniz: '))
final = int(input('finali giriniz: '))

ortalama = (vize1+vize2)*0.6+(final*0.4)

if ortalama > 50:
    if final >= 50:
        print('geçtiniz')
    else:
        print('kaldınız')
elif final >=70:
    print('geçtiniz')
else:
    print('kaldı')
'''
'''
ad = input('adınızı giriniz: ')
boy = float(input('boyunuzu giriniz: '))
kilo = float(input('kilonuzu giriniz: '))

indeks = (kilo/boy)**2

if indeks >= 0 and 18.4 >= indeks:
    print(f'{ad} zayıf.')
elif indeks >= 18.5 and 24.9 >= indeks:
    print(f'{ad} Normal.')
elif indeks >= 25.0 and 29.9 >= indeks:
    print(f'{ad} Fazla kilolu.')
elif indeks >= 30.0 and 34.9 >= indeks:
    print(f'{ad} Şişman.')
'''



















