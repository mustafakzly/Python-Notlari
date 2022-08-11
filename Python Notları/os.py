import os
import datetime
#result = dir(os)
#result =os.name

#klasör değiştirme
#os.chdir()
#os.chdir('..')
#os.rename("newdirectory","yeni_klasör")
#os.rmdir("yeni_klasör")
#os.removedir("yeni_klasör","yeniklasör")
#klasör oluşturur
#os.mkdir("newdirectory")
#os.makedirs("newdirectory/yeniklasör")
#listeleme
#result = os.listdir()
#result = os.listdir('C://')
#for dosya in os.listdir():
#   if dosya.endswith('.py'):
#       print(dosya)
#etkin dizin öğrenme
#result = os.getcwd()
#result = os.stat("datetime.py")
#result = result.st_size/1024  
#result = datetime.datetime.fromtimestamp(result.st_ctime)  
#result = datetime.datetime.fromtimestamp(result.st_atime) 
#result = datetime.datetime.fromtimestamp(result.st_mtime)   
#os.system("notepad.exe")

# path
result = os.path.abspath("datetime.py")
result = os.path.dirname("C:/Users/Mustafa/Desktop/Python/datetime.py")
result = os.path.dirname(os.path.abspath("datetime.py"))
result = os.path.exists("datetime.py")
result = os.path.isdir("C:/Users/Mustafa/Desktop/Python")#dosyaya bakar
result = os.path.isfile("C:/Users/Mustafa/Desktop/Python/datetime.py")
#result = os.path.join()
#result = os.path.split()
result = os.path.splitext("datetime.py")
result = result[1]
print(result)