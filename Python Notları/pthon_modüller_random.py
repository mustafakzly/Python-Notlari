import random

result = dir(random)

result = random.random() # 0.0 ve 1.0 arasında rastgele sayı üretme
result = random.random() * 100
result = int(random.uniform(5, 10))# üniform ondalıklı verir
result = random.randint(1, 8)# randint tam sayı verir

greeting = 'hello there'
names = ['ali','yağmur','deniz','cenk','ahmet','efe']
result = names[random.randint(0,len(names)-1)]
result = random.choice(names) # choice random isim seçme
result = random.choice(greeting)

liste = list(range(10))
random.shuffle(liste)
result = liste

liste = range(100)
result = random.sample(liste, 3) # sample kaç tane sayı aldığını gösterir
result = random.sample(names , 2)
print(result)