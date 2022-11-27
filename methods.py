'''
#Methods are functions declare within a class. Just like objects, they must take a parameter self
class stacks:
    def method(self, val):
        self.__mylist= [1,2,3,4,2,4,2,1,23,2,32,19,32,23,90,738,372,4,6,1998]
        if val in self.__mylist:
            print(val, ' is available')
        else:
            print(val, ' is not available')

g= stacks()
g.method(16)

class jack:
    def first_name(self):
        self.__name= 'Jack Watua'
        return print(self.__name)
    def method(self):
        print(self.var)
        self.first_name()
names= jack()
names.var= 'User First Name: '
names.method()

#Ypu can create a method as a constructor using the __init__ mrthod.
class jack:
    def __init__(self, val):
        self.list= val


g= jack(7)
g.val= 10
print(g.val)

#Creating private methods:



class jack:
    def visible(sefl):
        #This is a visible method
        print('Visible')
    def __invisible(self):
        #This is a hidden method. It means that it is only accessible or can only be invoked inside a class
        print('Hidden')
    def bal(self, val):
        self.__balance= val
    def __Abalance(self):
        print(self.__balance)

d= jack()
d.visible()
try:
    d.__invisible()
except:
    print('Failed')
# to access a private class through mangling: objectName._className__privateMethodName() for example 'd._jack__invisible_name


d._jack__invisible()
d.bal(7000)
d._jack__Abalance()
print(d.__module__)

class premier:
    def __init__(self, t=' Temporary'): # Method as a construcor
        #Isnstance variable
        self.__first_name= t # Private instance variable
    def change_first_name(self, val=0): #class 0bject
        self.__first_name= val #private Instance variable
    def getfull_names(self):
        self.p= self.__first_name + ' ' + self.secondName + ' ' +  self.thirdName
        return self.p
    def __method(self): #private method
        print(self.getfull_names())

    def visible(self): # visible method
        print('Visible')
    def __hidden(self): #private method
        print('hidden')
class trophies:
    pass
class tr(premier, trophies):
    pass
a= premier()# instance variable
b = tr
a.t= 'Jack'
a.secondName= 'Watua'
a.thirdName = 'Wanyonyi'
a.change_first_name('Jacob')
a._premier__method()
#invoking visible methods
a.visible()
try:
    a.__hidden() #This will raise an exceotion because the function/method is hidden
except:
    print('Failed!')
a._premier__hidden() #Here is the syntax for invoking a hidden method/function
# to know the original name of class in which an object belongs to, we use __name__ and a keyword 'type()'
print(type(a).__name__) #Returns 'Premier' i.e the class used to create the object
#To know the name of a superclass of an object. we use bases.
def Insprct(k):
    print('(', end=' ')
    for i in k.__bases__:
        print(i.__name__, end=' ')
    print(')')
Insprct(b)


#Introspection and Relflection. Inrtospection is cheking properties of an object at runtime. Reflection is the ability of a program to manipulate these properties
class jack: 
    pass
d= jack()
d.a= 1
d.b= 2
d.r= 9
d.ireal= 3.5
d.integer= 8
d.g= 20
d.q= 4
d.charity= 23


#to inspect if object d has an item starting with letter 'i'(introspect) and to alter it value by multiplying it by 5(reflect).
def introspect(d):
    for name in d.__dict__.keys(): # Gets the names of all the elements in the g__dictionary__
        if name.startswith('cha'): # identifies elements with names starting with letter'i' (integer and ireal)
            val= getattr(d, name)
            if isinstance(val, int):
                setattr(d, name, val - 1 )
introspect(d)
print(d.__dict__)
'''
class football:
    pass
class league (football):
    pass
class trophies(league):
    pass
class tr(trophies):
    pass
# to the name of a superclass to which an object belongs, we use __bases__

g= league()
g.total_teams= 16
g.season= '2020, 2021'
g.league= 'English premier league'

def printBase(k):
    print('(', end=' ')
    for i in k.__bases__:
        print(i.__name__, end=' ')
    print(')')
def Introspector(lj):
    for name in lj.__dict__.keys():
        if name.startswith('tot'):
            val= getattr(lj, name)
            if isinstance(val, int):
                setattr(lj, name, val + 4 )
Introspector(g)
print(g.__dict__)
print(isinstance(g, football))