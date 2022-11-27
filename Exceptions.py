def ty(a,b,c):
    try:
        f= a/b
        results = f * c
    except:
        print('Invalid action')
        results= None
    else:
        print('Good to go')
    finally:
        print('Time to say Goodbye')
        return results

class pizzaError(Exception):
    def __init__(self, pizza, message):
        super().__init__(message)
        self.pizza= pizza
class tooMuchCheesError(pizzaError):
    def __init__(self, pizza, cheese, message):
        super().__init__(pizza, message)
        self.cheese= cheese


def makepizza(pizza, cheese):
    if pizza not in ['Peparoni', 'Periperi', 'Bacon', 'Chicken Beef']:
        raise pizzaError(pizza, 'Not so much on the menu')
    if cheese > 100:
        raise tooMuchCheesError(pizza, cheese, 'Has too much cheese')
    print('Pizza is ready')
try:
    makepizza('Peparoni', 100)
except tooMuchCheesError as tmce:
    print(tmce, ':', tmce.cheese)
except pizzaError as pe:
    print(pe, ':', pe.pizza)


class nameError(Exception):
    def __init__(self, name= 'Edwin Okemwa', netWorth= 10000):
        super().__init__(netWorth)
        self.name= name
        self.networth= netWorth

class newUser(nameError):
    def __init__(self, marital, new_netWorth, ):
        super().__init__(netWorth=new_netWorth)
        self.marital= marital


