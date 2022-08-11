numbers =[]

for x in range(10):
    numbers.append(x)
print(numbers)

numbers = [x for x in range(10)]
print(numbers)

number = [x**2 for x in range(10)]
print(number)

number = [x*x for x in range(10) if x%3 ==0]
print(number)

myString = 'hello'
myList = [letter for letter in myString]
print(myList)

results =[x if x%2 == 0 else 'tek' for x in range(1,10)]
print(results)

numbers = [(x,y) for x in range(3) for y in range(3)]
print(numbers)