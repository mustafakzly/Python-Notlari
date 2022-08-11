#x = int(input('bir sayı giriniz: '))
#result = x <= 100 and x >= 0
#print(f"{x} sayısı 0 ile 100 arasında mı : {result}")

#y = int(input('bir sayı giriniz: '))
#result1 = (y%2 == 0) and y > 0
#print(f"{y} pozitif çift sayı mı : {result1}")

#q = int(input('birinci sayıyı giriniz: '))
#w = int(input('ikinci sayıyı giriniz: '))
#e = int(input('üçüncü sayıyı giriniz: '))
#result3 = q>w and q>e
#result4 = w>e and w>q
#result5 = e>q and e>w
#print(f"{q} en büyük mü: {result3} {w} en büyük mü: {result4} {e} en büyük mü: {result5}")


#vize1 = int(input('vize1 giriniz: '))
#vize2 = int(input('vize2 giriniz: '))
#final = int(input('final giriniz: '))

#ortalama = ((vize1+vize2)*0.6)+(final*0.4)

#result6 = ortalama > 50
#print(f"{ortalama} geçtin mi kaldın mı: {result6}")

#result7 = ortalama >= 50 and final > 50
#print(f"{ortalama} ortalamanız, final notu {final} geçtin mi kaldın mı: {result7}")

#result8 = final > 70
#print(f"{final} final notunuz geçtin mi kaldın mı: {result8}")

ad = input('adınızı giriniz: ')
kilo = int(input('kilo giriniz: '))
boy = float(input('boy giriniz: '))
indeks = (kilo/boy)**2
zayif = indeks>0 and indeks <=18.4
normal = indeks>=18.5 and indeks <=24.9
fazla_kilolu = indeks>=25.0 and indeks <=29.9
sisman = indeks>=30.0 and indeks <=34.9

print(f"{ad} {kilo} {boy} {indeks} sizin indeksiniz durmunuz: zayıf : {zayif} normal: {normal} fazla kilolu: {fazla_kilolu} sisman : {sisman}")