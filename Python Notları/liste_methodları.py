numbers = [1,10,5,16,4,9,10]
letters =['a','g','s','b','y','a','s']

val = min(numbers)
val = max(numbers)
val = max(letters)
val = min(letters)
val = numbers[0:3]
val = numbers[:3]
val = numbers[4:]

numbers[4] = 40
numbers.append(15) # en sona ekleme yapar
numbers.insert(3, 45) # 3. indexe 45 sayısını ekler
numbers.pop(4) # êleman siler
numbers.remove(5) # verilen elemanı siler
numbers.sort() #sayısal olarak sıralar
letters.sort() # alfabetik olarak sıralar
numbers.reverse() #ters çevirir
letters.reverse() #ters çevirir
numbers.clear() #bütün elemanları siler
print(val)
print(letters.count('a'))