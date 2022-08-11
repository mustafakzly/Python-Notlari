#x = int(input('birinci sayı giriniz: '))
#y = int(input('ikinci sayı giriniz: '))

#result = x > y
#print(result)

#vize1 = int(input('1. vize giriniz: '))
#vize2 = int(input('2. vize giriniz: '))
#final = int(input('final giriniz: '))

#ortalama =((vize1+vize2)*0.6)+(final*0.4)
#print(f"not ortalamanız : {ortalama} ve dersten geçme durumunuz: {ortalama>=50}")

#sayi = int(input('sayı : '))
#tekcift = (sayi%2 == 0)
#print(tekcift)

#sayi = int(input('sayı : '))
#pozitifmi = sayi > 0 
#print(pozitifmi)

email = 'mustafa@gmail.com'
password = '12345678'

girilenMail = input('email: ')
girilenPassword = input('parola: ')

isMail = (email==girilenMail.lower().strip())
isPassword = (password==girilenPassword)

print(f"Email bilgisi doğru mu : {isMail} Password bilgisi doğru mu : {isPassword}")