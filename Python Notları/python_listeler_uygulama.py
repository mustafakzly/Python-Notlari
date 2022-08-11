cars = ['BMW', 'Mercedes', 'Opel', 'Mazda']

result = len(cars)
result = cars[0]
result = cars[3]
result = cars[-1]


result = cars[-2]

result = cars[0:3]

cars[-2:] = ['toyota', 'renault']

#cars[-1] = 'toyota'
result = cars

result = 'Mercedes' in cars
result = cars + ['audi', 'nissan']

del cars[-1]
result = cars

result = cars[::-1]

studentA = ['Yiğit', 'Bilgi', 2010, [70,60,70]]
studentB = ['Sena', 'Turan', 1999, [80,80,70]]
studentC = ['Ahmet', 'Turan', 1998, [80,70,90]]

result = studentA[0]
result = studentB[1]
result = studentC[3][1]

result = f"{studentA[0]} {studentA[1]} {2022-studentA[2]} yaşında ve not ortalaması {(studentA[3][0]+studentA[3][1]+studentA[3][2])/3}"