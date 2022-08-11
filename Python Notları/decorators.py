#def decorator(fonk):
#    def wrapper():
#        print("fonksiyon çalışmadan önceki işlemler")
#        fonk()
#        print("fonksiyon çalıştıktan sonraki işlemler")
#    return wrapper
#    
#@decorator    
#def fonksiyon():
#    print("fonksiyon çalışıyor.")
#    
#fonksiyon()
import time
def zaman_hesaplama(fonk):
    def wrapper(*args,**kwargs):
        baslangıc = time.time()
        fonk(*args,**kwargs)
        bitis = time.time()
        print(f"işlem {bitis-baslangıc} saniye sürdü.")
    return wrapper
        
@zaman_hesaplama
def kareleri_al(liste):
    for i in liste:
        print(i*i)
@zaman_hesaplama
def kupleri_al(liste):
    for i in liste:
        print(i**3)
@zaman_hesaplama      
def topla(a,b):
    time.sleep(1)
    print(a+b)

topla(10,20)