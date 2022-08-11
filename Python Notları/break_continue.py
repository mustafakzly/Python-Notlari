name = 'mustafa kızılay'
'''
for letter in name:
    if letter == 'z':
        break 
    print(letter)
'''
'''
for letter in name:
    if letter == 'f':
        continue
    print(letter)
'''
'''
x = 0

while x < 5:
    x+=1
    if x == 2:
        continue
    print(x)
'''

x = 1 
result = 0

while x <= 100:
    if x % 2 == 1:
        continue
    result +=x
    x+=1