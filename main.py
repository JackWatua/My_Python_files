class pizzaError(Exception):
    def __init__(self, pizza, message= 'Too Much'):
        Exception.__init__(message)
        self.pizza= pizza
class ka:
    def __init__(self, pizza= 'Bacon', cheese= 1):
        self.pizza= pizza
        self.cheese= cheese
        self.message= 'Temporary Message! '
class make_pizza(ka):
    def __init__(self,cheese, pizza=' '):
        super().__init__()
        self.va= pizza
        self.cheese= cheese
a= ka('Bacon', 75)
b= make_pizza('60')

def test(pizzza):
    if pizzza != 'Peparoni':
        raise pizzaError
    print('Not ', pizzza)

test('poppo')