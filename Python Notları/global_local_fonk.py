'''
#global scope
x = 'global x'

def function():
    #local scope
    x = 'local x'
function()
print(x)
''' 
'''
name = 'mustafa'

def changeName(new_name):
    name = new_name
    print(name)
    
changeName('hüseyin')
print(name)
''' 
'''
name = 'global string'

def greeting():
    name = 'mustafa'
    def hello():
        print('hello ' + name)
    hello()
greeting()
'''

x = 50

def test(x):
    print(f'x = {x}')
    x= 100
    print(f'change x to {x}' )
test(x)