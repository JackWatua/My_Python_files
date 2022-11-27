users= ['Jack', 'Bill', 'Charity', 'Cynthia', 'Dan']
def push(g):
    users.append(g)
def pop():
    g= users [-1]
    del users [-1]
    return g
def get_user(d):
    try:
        for i in range(d):
            yield users[i]
    except IndexError:
        print('Not available')
    except:
        print('Invalid')
push('Roy')
push('Jadol')
push('Erick')
push('Jemimah')
push('Brian')

def fibonacci(n):
    p=pp=1
    for i in range(n):
        if i in[0,1]:
            yield 1
        else:
            n= p + pp
            pp, p = p, n
            yield n
v= (list(get_user(5)))
print(v)
