'''
#class creates a class and names it jackwatua, add a colon because classes just like functions form their own nested blocks. Pass is a key word that fills the class with nothing(i.e no methods or properties)

class jackWatua:
    pass
#The object below inerits all properties that the class contains. In this case the class is emtpty and so is the object.
#The process of creating an object from as is called instantation as it creates an instance of the class.
my_object= jackWatua()

stack=[]
def push(val):
    stack.append(val)
def pop():
    val= stack[-1]
    del stack[-1]
    return stack
push(1)
push (2)
push (3)
print(pop())
print(pop())
print(pop())
'''
# To create objects within classes, we use consructors. __init__. A constuctor takes at least one arguement.
# The obligatory parameter is always self. 
'''
class ja:
    def __init__(self):
        print('Hello jacob')

b= ja()
# self is used to pass properties to class objects
class jack:
    def __init__(self):
        self.list= []
        a= 0
        while a> 10:
            a+=1
            self.list.append(a)
            print(self.list)
d= jack()

# Stacks. Adding functions within a class and invoking them
# Objects created from the same class act independently
class stacks:
    def __init__(self):
        self.__my_list= []
    def push(self, val):
        self.__my_list.append(val)
    def pop(self):
        val= self.__my_list[-1]
        del self.__my_list[-1]
        return val
class stacks_add(stacks):
    def __init__(self):
        stacks.__init__(self)
        self.__sum= 0
    def get_sum (self):
        return self.__sum
    def push(self, val):
        self.__sum+=val
        stacks.push(self, val)
    def pop(self):
        val= stacks.pop(self)
        self.__sum -= val
        return val
    
b= stacks_add()
b.push(19)
print((b.get_sum()))

#Instances 
class jack:
    def __init__(self, val=1):
        self.__first= val
    def set_second(self, val):
        self.__second= val
#to create instances
we= jack()
we.set_second(3)
wr= jack(8)
wr.set_second(10)
#This creates a new property and assigns it a name 'third' and a value of 5.
wr.third= 5
#To know all the properties in an instance
print(we.__dict__)
print(wr.__dict__)
#We can access individual properties as follows.
print(we._jack__first)
print(wr._jack__second)
print(wr.third)




# class variables. A class variable is a property that exists just in one copy and is stored outside any object.



class jack:
    Counter= 0
    def __init__(self, val=1):
        self.__first= val
        jack.Counter+=1
v= jack()
print(v.__dict__, v.Counter)
w= jack(3)
print(w.__dict__, w.Counter)
z= jack(20)
print(z.__dict__, z.Counter)
'''
#checking if attributes exist using hasattr(a,b) function
class jack:
    def __init__(self, val):
        self.__months= ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
        self.g= int(val[3:5])
        self.h= int(val[6:])
        if self.g > 12:
            print('Month out of range!!')
            return
        else:
            if self.h< 1950 or self.h >2021:
                print('Year is out of range(', self.h,')')
                self.Birthday_month= None
                return
            else:
                self.Birthday_month= self.__months[self.g-1]
    def get_bdaymonth(self):
        return self.Birthday_month
try:
    c= jack('08/er4/2022')
    print(c.get_bdaymonth())
except ValueError:
    print('Invalid Action')


