# dosya açmak ve oluşturmak için open() fonksiyonu kullanılır
#kullanımı: open(dosya_adi,dosya_erişme_modu)
#dosya_erişme_modu => dosyayı hangi amaçla açtığımızı belirtir

# "w" (write) yazma modu. dosyayı konumda oluşturur.

#file = open("newfile.txt","w")
#file.close()
#file = open("C:/Users/Mustafa/Desktop/fidarv2/newfile.txt","w")
#print(file)

#file = open("newfile.txt","w",encoding ='utf-8')
#file.write("mustafa kızılay")
#file.close()
# "a" (append) ekleme. Dosya konumda yoksa oluşturur.
#file = open("newfile.txt","a",encoding ='utf-8')
#file.write("mustafa kızılay")
#file.close()
# "x" (create) oluştumra. dosya zaten varsa  hata verir.
#file = open("newfile2.txt","x",encoding ='utf-8')

# "r" (read) okuma. varsayılan. dosya konumda yoksa hata verir.
"""
try:
    file = open("newfile.txt","r")
except FileNotFoundError:
    print("dosya okuma hatası")
finally:
    print("dosya kapandı")
    file.close()
print(file)
"""

file = open("newfile.txt","r")
#for döngüsü
"""
#for i in file:
#    print(i, end = "")

#read() fonksiyonu

content = file.read()
print(content)

content = file.read(5)
print(content)
file.close()
"""

#readline() fonksiyonu

print(file.readline())

#readlines() fonksiyonu

liste = file.readlines()

print(liste)
file.close()