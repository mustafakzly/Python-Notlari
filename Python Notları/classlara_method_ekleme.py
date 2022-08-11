#class
'''
class Person:
    pass
    # class attributes
    address = 'no information'
    #constructor (yapıcı method)
    def __init__(self, name, year):
    #self = p1 ve p2
    # object attributes
        self.name = name
        self.year = year
        print('init methodu çalıştı')
    # instance methods
    def intro(self):
        print('hello there. I am '+ self.name)
    # instance methods
    def calculateAge(self):
        return 2022 - self.year
    
#object (instance)
p1 = Person('mustafa', 2000)
p2 = Person('hüseyin', 1992)

p1.intro()
p2.intro()
print(f"adım : {p1.name} yaşım : {p1.calculateAge()}")
print(f"adım : {p2.name} yaşım : {p2.calculateAge()}")
'''

class Circle:
    #class object attribute
    pi = 3.14

    def __init__(self,yaricap = 1):
        self.yaricap = yaricap
        
    #method
    def cevreHesapla(self):
        return 2 * self.pi * self.yaricap
    def alanHesapla(self):
        return self.pi * (self.yaricap**2)
    
c1 = Circle()
c2 = Circle(5)

print(f"c1 : alan = {c1.alanHesapla()} çevre = {c1.cevreHesapla()}")
print(f"c2 : alan = {c2.alanHesapla()} çevre = {c1.cevreHesapla()}")