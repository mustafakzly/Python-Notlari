"""
def cube():
    result = []
    for i in range(5):
        yield i**3

iterator = cube()

for i in iterator:
    print(i)
    
"""

generator = (i**3 for i in range(5))
print(generator)

print(next(generator))