'''
def changeName(n):
    n = 'mustafa'
    
name = 'hüseyin'
changeName('name')
print(name)

def change(n):
    n[0] = 'istanbul'
    
sehirler = ['ankara','izmir']
change(sehirler[:])
print(sehirler)
'''
'''
def add(a,b, c = 0):
    return sum((a,b,c))
print(add(10,20))
print(add(10,20,30))
'''
'''
def add(*params):
    return sum((params))
print(add(10,20))
print(add(10,20,30))
'''
'''
def add(*params):
   sum = 0
   
   for i in params:
       sum = sum+i
   return sum    
print(add(10,20))
print(add(10,20,30))
'''

def displayUser(**params):
    for key, value in params.items():
        print('{} is {}'.format(key, value))

displayUser(name = 'mustafa', yas = '22', sehir = 'niğde')
displayUser(name = 'hüseyin', yas = '29', sehir = 'ankara', phone ='123123')
displayUser(name = 'ünver', yas = '31', sehir = 'kocaeli', phone ='1232123', email = 'hsdaha@gmail.com')

































