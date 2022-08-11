# map methodu ya listeyle ya da for dögüsünde kullanılmalı
'''
def square(num): return num**2
numbers = [1,2,3,4,5]
result = list(map(square,numbers))
print(result)
    
for item in map(square,numbers):
    print(item)

result1 = list(map(lambda num: num**3,numbers))
print(result1)
'''
numbers = [1,2,3,4,5]
def check_even(num):
    return num%2 == 0
result = list(filter(check_even, numbers))
print(result)