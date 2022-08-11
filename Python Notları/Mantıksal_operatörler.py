x = 6
hak = 5
devam = "e"
result = 5 < x < 10
print(result)

#and eşitliğin iki tarafı da doğru olmalı

result1 = x > 5 and x < 10
result2 = (hak > 0) and (devam == 'e' )
print(result1, result2)

#or eşitliğin bir tarafının doğru olması yeterli

result3 = (x > 0) or (x % 2 == 0)
print(result3)

#not

result4 = not(x > 0)
print(result4)