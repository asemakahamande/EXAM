i = [1,2,3,4,5]
m = map(lambda x: 2**x, i)
print(list(m))


y = [2, 5, 6]
y.sort()
print(y)

class Welcome:
    def __init__(self, name):
        self.name=name

    def say_hello(self):
        print('Welcome to', self.name)

cw = Welcome('Turing')
cw.say_hello()
def mygenerator():
    print('First item')
    yield 10

    print('Second item')
    yield 20

    print('Last item')
    yield 30
print(mygenerator)