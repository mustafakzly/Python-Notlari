#liste = [1,2,3,4,5]

#iterator = iter(liste)
#print(iterator)

#print(next(iterator))
#print(next(iterator))
#print(next(iterator))
"""
while True:
    try:
        element = next(iterator)
        print(element)
    except StopIteration:
        break
"""

class MyNumbers:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __iter__(self):
        return self
    def __next__(self):
        if self.a <= self.b:
            x = self.a
            self.a+=1
            return x
        else:
            raise StopIteration
            
list =  MyNumbers(10,50)
for x in list:
    print(x)