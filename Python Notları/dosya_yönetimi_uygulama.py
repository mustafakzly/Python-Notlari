def not_hesapla(satir):
    satir = satir[:-1]
    liste = satir.split[':']
    ogrenciAdi = liste[0]
    notlar = liste[1].split(',')

    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])
    
    ortalama = (not1+not2+not3)/3
    
    if ortalama >= 90 and ortalama <= 100:
        harf = "AA"
    elif ortalama >= 85 and ortalama <=89:
        harf = "BA"
    elif ortalama >= 65 and ortalama <=84:
        harf = "CC"
    else:
        harf = "FF"
    return ogrenciAdi + ":" + harf + "\n"
def ortalamalari_oku():
    with open("sinav_notlari.txt","r") as file:
        for satir in file:
            print(not_hesapla(satir))
def not_gir():
    ad = input('Ögrenci adı: ')
    soyad = input('Ögrenci soyad: ')
    not1 = input('not 1: ')
    not2 = input('not 2: ')
    not3 = input('not 3: ')
    
    with open("sinav_notlari.txt","a") as file :
       file.write(ad + ' ' + soyad + ':'+ not1+','+not2+','+not3+'\n')     
def notlari_kayitet():
    pass
while True:
    islem = input('1- Notları Oku\n2-Not Gir\n3- Notları kayıt et\n4-Çıkış\n')
    if islem == '1':
        ortalamalari_oku()
    elif islem == '2':
        not_gir()
    elif islem == '3':
        pass
    else:
        break