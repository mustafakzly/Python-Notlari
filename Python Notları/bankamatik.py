MustafaHesap = {
    'ad': 'Mustafa Kızılay',
    'hesapNo': '123456',
    'bakiye' : 3000,
    'ekHesap' : 2000
    }
HuseyinHesap = {
    'ad': 'Hüseyin Kızılay',
    'hesapNo': '123457',
    'bakiye' : 5000,
    'ekHesap' : 3000
    }

def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")
    
    if (hesap['bakiye'] >= miktar):
        hesap['bakiye'] -= miktar
        print('paranızı alabilirsiniz.')
    else:
        toplam = hesap['bakiye']+ hesap['ekHesap']
        if(toplam >= miktar):
            ekHesapKullanimi = input('ek hesap kullanılsın mı (e/h) ')
            if ekHesapKullanimi == 'e':
                ekhesaptankullanilacakpara = miktar - hesap['bakiye']
                hesap['bakiye']
                print('paranızı alabilirsiniz.')
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} bulunmaktadır.")
        else:
            print('üzgünüz bakiye yetersiz.')
paraCek(MustafaHesap,4000)