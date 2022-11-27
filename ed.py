class pizzaError(Exception):
    def __init__(self, pizza, message):
        super().__init__(message)
        self.message= message
        self.pizza= pizza
class CheeseError(pizzaError):
    def __init__(self, pizza, cheese, message):
        super().__init__(pizza=pizza, message=message)
        self.cheese= cheese
        self.pizza= pizza
def make_pizza(pizza, cheese, message):
        if cheese <40:
             raise CheeseError(pizza, cheese, 'Too litle cheese in the pizza')
        elif cheese>100:
            raise CheeseError(pizza, cheese, message)
        print ('Pizza is ready')
h= CheeseError('Peparoni', 139, 'Too much cheese in the pizza')
h.Guapo= 89
def intrspct(c):
    for name in c.__dict__.keys():
        if name.startswith('Guapo'):
            val= getattr(c, name)
            if isinstance(c, int):
                setattr(c, name, val+1)
