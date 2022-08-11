#range
'''
for item in range(50,100,5):
    print(item)

print(list(range(50,100,5)))
'''

#enumerate
'''
greeting = 'hello there'

for letter in enumerate(greeting):
    print(letter)
'''

#zip

list1 = [1,2,3,4,5]
list2 = ['a','b','c','d','f']
list3 = [100,200,300,400,500]

print(list(zip(list1,list2,list3)))

for list in zip(list1,list2,list3):
    print(list)