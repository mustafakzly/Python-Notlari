kare_al = lambda x : x * x

kup_al = lambda x : x ** 3

toplam = lambda a,b : a + b

genel_toplam = lambda *args : sum(args)

print(genel_toplam(2,3,5,6,7))

print((lambda x,y,z : x*y+z)(3,5,6))
print((lambda *args : sum(args)/len(args))(2,3,4,5,6,7,8))