class Kisi:
    def __init__(self,ad,soyad):
        self.ad = ad
        self.soyad = soyad
        #self.adsoyad = ad + " " + soyad
    @property
    def adsoyad(self):
        return f"{self.ad}.{self.soyad}"
    @property
    def email(self):
        return f"{self.ad}.{self.soyad}@sirket.com"
    @adsoyad.setter
    def adsoyad(self,isim):
        ad,soyad = isim.split(" ")
        self.ad = ad
        self.soyad = soyad
    @adsoyad.deleter 
    def adsoyad(self):
        print("silindi")
        self.ad = None
        self.soyad = None
        
# property methodlara özellik gibi erişiyor    
kisi1 = Kisi("mustafa","kızılay")
kisi1.ad = "hüseyin"
kisi1.adsoyad = "Ayşe yılmaz"
del kisi1.adsoyad
print(kisi1.ad)
print(kisi1.adsoyad)
print(kisi1.email)