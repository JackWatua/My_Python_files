'''
#Inheritance and why
class t:
    def __init__(self, name, galaxy):
        self.name= name
        self.galaxy= galaxy
    def __str(self):
        return self.name + ' in ' + self.galaxy
sun= t('Sun', 'Milky Way')
print(sun._t__str())

# If B is a subclass of A and C is a subclass of B, C is also a subclass of A and the re;ationship is fully transitive
class vehicle:
    pass
class LandVehicle(vehicle): #subclass of vehicles
    pass
class TrackedVehicle(LandVehicle): #subclass of both vehicles and Landvehicles
    pass
#To check for inherritance in classes... we use issubclass(classs, subclass)
def get_class_1():
    for t1 in [vehicle, LandVehicle, TrackedVehicle]:
        for t2 in [vehicle, LandVehicle, TrackedVehicle]:
            print(issubclass(t1 , t2), end = " ")
        print()
#We can also use print(issubclass()) to check if an object belongs to a certain class
def PrintSubClass():
    print(issubclass(TrackedVehicle, vehicle))

# Now let us create some objects and see how we can check is objects have attributes similar to that of a superclass
obt_1= vehicle()
obt_2= LandVehicle()
obt_3= TrackedVehicle()
# To check if an object belongs to a certain class or not, we use issinstance(Object, Class). As follows
def get_class():
    for i in[obt_1, obt_2, obt_3]:
        for r in [vehicle, LandVehicle, TrackedVehicle]:
            if isinstance(i, r):
                print(type(i).__name__ ,'is an instance or an object in ',r.__name__)
            else:
                print(type(i).__name__ ,'is not an instance or an object in ',r.__name__)
get_class()


#The 'is' operator. The is opetor checks to see if two refer to the same object. W

class ob:
    def __init__(self, val):
        self.sample= val


obj_1= ob(5)
obj_2= ob(0)
obj_3= obj_1
obj_3.sample -=5 


print(obj_1.sample)
class Supper:
    Counter= 0
    def __init__(self, n1= 'Sample'):
        self.user_passWord= n1
        self.oe= 57
    def __str__(self):
        return 'User password: ' + self.user_passWord + '\n ' + 'User ID :' + str(self.oe)
    def f(self):
        return Supper.Counter
class Sub1(Supper):
    def __init__(self, n2):
        super().__init__(n1=n2)
        self.new_password = n2
        self.oe += 3
        Supper.Counter +=1
class Sub2(Sub1):
    def __init__(self):
        pass
    
d= Supper('Watua_Jack')
obj= Sub1('JackWatua254')
print(d)
print(obj)
'''