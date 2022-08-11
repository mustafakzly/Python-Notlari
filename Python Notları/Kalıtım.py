# inheritance (kalıtım): miras alma

# person => name, lastname, age, eat(), run(), drink()
# person için kullanılan her şey student ve teacher için de kullanılmalı
# student(Person), teacher(Person)


# animal => dog(Animal), cat(Animal)


class Person():
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname
        print('Person Create')
    
    def who_am_i():
        print('I am a person')
    def eat():
        print("i am eating")

class Student(Person):
    def __init__(self,fname,lname, number):
        Person.__init__(self,fname,lname)
        self.studentNumber = number
        print('Student Created')
    # override
    def who_am_i():
        print('I am a student')
    def sayHello():
        print('Hello i am a student')

class Teacher(Person):
    def __init__(self,fname,lname, branch):
        super().__init__(fname,lname)
        self.branch = branch
    def who_am_i(self):
        print(f'i am a {self.branch} teacher')
        
    

p1 = Person('mustafa','kızılay')
s1 = Student('hüseyin','kızılay','1234')
t1 = Teacher('ünver','kızılay')
print(p1.firstName + ' ' + p1.lastName)
print(s1.firstName + ' ' + s1.lastName + ' ' + str(s1.studentNumber))
   
t1.who_am_i()