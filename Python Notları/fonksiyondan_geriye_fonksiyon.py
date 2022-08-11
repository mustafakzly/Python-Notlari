#def topla(x,y):
#    return x+y
#def carpma(x,y):
#    return x*y
#def islemYap(fonk,a,b):
#    return fonk(a,b)

#print(islemYap(topla,3,5))
#print(islemYap(carpma,3,5))

#liste = [1,2,3,4,5,6,7,8]
#fonk = x*x
#sonuc = [1,4,9,16,25,36,49,64

liste1 = [1,2,3,4,5]
liste2 = [1,3,4,5,8,9,11]

def kare_al(x):
    return x*x
def kup_al(x):
    return x**3

def map_fonk(fonk,liste):
    sonuc = []
    for i in liste:
        sonuc.append(fonk(i))
    return sonuc
print(map_fonk(kup_al,liste2))
        
    