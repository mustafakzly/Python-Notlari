ogrenciler = {
    
 
}


number = input('ogrenci no: ')
name = input('ogrenci adı: ')
surname = input('ogrenci soyad: ')
phone = input('ogrenci telefon: ')

'''

ogrenciler [number] = {
    'ad': name,
    'soyad': surname,
    'telefon': phone
    }

'''
ogrenciler.update({
    number:{
        'ad': name,
        'soyad':surname,
        'telefon':phone
        }    
})
ogrNo = input('ogrenci numarası giriniz: ')
ogrenci = ogrenciler[ogrNo]
print(f"Aradığınız {ogrNo} nolu öğrencinin adı: {ogrenci['ad']} soyadı: {ogrenci['soyad']} telefon no: {ogrenci['telefon']} bu ögrenciye aittir")

