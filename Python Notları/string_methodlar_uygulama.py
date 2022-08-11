website = "http://www.sadikturan.com"
course = "Python kursu: bastan sona python progormalama rehberiniz (40 saat)"

result = ' Hello World '.strip()
result = ' Hello World '.lstrip()#soldan boşluğu siler
result = ' Hello World '.rstrip()#sağdan boşluğu siler

result = "www.sadikturan.com".strip('w.moc') #sadikturan yazısını alır

result = course.upper()

result = website.count('a') #kaç tane a harfi var

result = website.startswith('www')
result = website.endswith('com')

result = website.find('com')
result = website.index('com')

result = course.isalpha()# Alfabetik mi
result = 'hello'.isalpha()
result = course.isdigit()# sayısal mı
result = '123'.isdigit()

result = 'Contents'.center(50,'^')
result = 'Contents'.ljust(50,'^') #contents sola yaslar
result = 'Contents'.rjust(50,'^') #contents sağa yaslar

result = course.replace(' ', '-')

result = 'Hello world'.replace('world', 'there')

result = result.split(' ')
result = result[1]