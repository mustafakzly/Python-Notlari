name = 'mustafa'
surname = 'KIZILAY'
yas = '22'
print('My name is {} {}'.format(name, surname))
print('My name is {1} {0}'.format(name, surname))
print('My name is {s} {n}'.format(n=name, s=surname))
print("My name is {n} {s} and I'm {y} years old ".format(n=name, s=surname , y=yas))

result = 200/700
print ('the result is {r:1.4}'.format(r=result))



print(f"My name is {name} {surname} and I'm {yas} years old ")
