'''
def yazdir(kelime, adet):
    print(kelime*adet)
    
yazdir('mustafa\n',10)
'''

'''
def list1(*params):
    list = []
    
    for param in params:
        list.append(param)
    return list

result = list1(10,20,30,'mercedes')
print(result)
'''
'''
def asalbulma(sayi1,sayi2):
    for sayi in range(sayi1,sayi2+1):
        if sayi > 1:
            for i in range(2,sayi):
                if sayi % i == 0:
                    break
            else:
                print(sayi)


sayi1 = int(input('bir sayi giriniz: '))
sayi2 = int(input('bir sayi giriniz: '))
asalbulma(sayi1,sayi2)    
'''
'''
def tamBolen(sayi):
    tambolenler = []
    
    for i in range(2,sayi):
        if sayi % i == 0 :
            tambolenler.append(i)
    return tambolenler

print(tamBolen(20))     
'''