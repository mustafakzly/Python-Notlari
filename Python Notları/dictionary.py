'''
sehirler = ['kocaeli','istanbul']
plakalar = ['41','34']

print(plakalar[sehirler.index('kocaeli')])
# key value değeri olarak yazdırdık
plakalar = {'kocaeli':41, 'istanbul':34}
print(plakalar['kocaeli'])
print(plakalar['istanbul'])

plakalar['ankara'] = 6
plakalar['kocaeli'] = 'new value'

print(plakalar)
'''

users = {
    'mustafa kızılay':{
        'age':22,
        'roles': ['admin','user'],
        'email': 'mustafa@gmail.com',
        'adres': 'nigde',
        'phone' : '12312321312'
        
        
    },
    'hüseyin kızılay':{
        'age':29,
        'roles': ['user'],
        'email': 'hüseyin@gmail.com',
        'adres': 'ankara',
        'phone' : '12442321312'
        
        
    }   
}

print(users['mustafa kızılay']['roles'][0])