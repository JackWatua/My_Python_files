'''
list_1= []
for i in range(10):
    list_1.append(10 **i)
list_2= [10**i for i in range(10)]

print(list_1)
print(list_2)
list_d= []
for i in range(10):
    list_d.append(1 if i % 2==0 else 0)
print(list_d)

list_e=[1 if i % 2==0 else 0 for i in range(10)]
print(list_e)
generator= (1 if i % 2== 0 else 0 for i in range(10))
print(generator)







for i in range(5):
    print(sqr(i))

import time
#Lets comprehend some lists
def message():
    print('Enter items separated with commmas, no spaces!')
def test(naes_1):
    
    n= naes_1.split(',')
    b= list(n)
    c=[b[e].title() for e in range(10)]
    print(b)
    print(c)
    
message()
time.sleep(5)
ht= input('Type here: ')
test(ht)

#lambda. Lambda is a finction wihtout a name/ anonymous

num= lambda: 2
sqr= lambda x: x * x
pwr= lambda x, y: x ** y
roots= []
powers= []
for i in range(10):
    roots.append(sqr(i))
    powers.append(pwr(i, num()))
print(roots)
print(powers)

#What are lambdas used for? Lambdas are anonymus parts of code intended to evaluate a result.
def print_function(x, fun):
    for x in x:
        print('f(',x,')=', fun(x), sep=' ')
print_function([x for x in range(-2, 3)], lambda x:(2*((x)**2)-(4*(x)) + 2))

# We can use the map(function, list) to apply a function to all elements of a list
list_1= [1 if x%2==0 else x for x in range(5)]
list_2= list(map(lambda x: x**2, list_1))
list_3= list(map(lambda x: x*2, list_2))


from random import randint, random

d= [randint(5,10) for c in range(5)]
f= list(filter(lambda x: x>0 and x%2==0, d))
print(d)
print(f)
'''
#closure
def par(v):
    rt= v
    def closy():
        return str(rt) + ' It is'
    return closy
var= 1
fun= par(var)
print(fun())