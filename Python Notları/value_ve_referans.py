#value types => string,numbers
x = 5
y = 25

x = y
y = 10
print(x,y)
# sonuç 25 10
#referance types => list

a = ['apple','banana']
b = ['apple','banana']

a = b

b[0] = 'grape'

print(a,b)
# sonuç grape banana grape banana