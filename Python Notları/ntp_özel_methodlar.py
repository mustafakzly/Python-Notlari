mylist = [1,2,3,4]
myString = 'my string'
print(len(mylist))
print(len(myString))
print(mylist,'\n',myString)
class Movie():
    def __init__(self,title,director,duration):
        self.title = title
        self.director = director
        self.duration = duration
        print('movie objesi oluşturuldu')
    def __str__(self):
        return f"{self.title} by {self.director}"
    def __len__(self):
        return self.duration
    def __del__(self):
        print('movie objesi silindi')
m = Movie('film adı','yönetmen adı', 120)
print(type(m))

#print(mylist)
#print(m)

#print(len(mylist))
#print(len(m))

del m
print(m)