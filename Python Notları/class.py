#class

class Person:
    pass
    # class attributes
    address = 'no information'
    #constructor (yapıcı method)
    def __init__(this, name, year):
    #self = p1 ve p2
    # object attributes
        this.name = name
        this.year = year
        print('init methodu çalıştı')
    #methods
    
    
#object (instance)
p1 = Person('mustafa', 2000)
p2 = Person('hüseyin', 1992)
#updating
p1.name = 'ünver'
p1.address = 'Nidğe'
#accessing object attributes
print(f"p1 : name: {p1.name} year. {p1.year} address: {p1.address}")
print(f"p2 : name: {p2.name} year. {p2.year} address: {p2.address}")

print(type(p1))
print(type(p2))