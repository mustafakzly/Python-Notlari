sayi = int(input('bir sayi giriniz : '))
asalmi = True
if sayi == 1:
    asalmi = False
for i in range(2,sayi):
    if sayi%i == 0:
        asalmi = False
        break
if asalmi == True:
    print("sayi asaldır.")
else:
    print('sayi asal değildir.')
    