def q1():
    print("hello" * 5)


def q2():
    x,y= 4, 5
    y,x= x, y
    print(x)
    print(y)

def q3():
    z=9
    f = [0] * z
    print(f[:-1])
def q4():
    def help(x):
        return x % 2 == 0
    k=[i**2 for i in range(10)]
    k=filter(help, k)
    print(list(k)[::2])
def q5():
    p= 0
    for i in range(1, 10):
        if (i + 1 // 2) % 7 == 0:
            break
        else:
            p += int(i % 2 == 0)
            print(p)
    else:
        print('end')

def q6():
    import math

    for i in range(1, 100):
        if math.sqrt(i) == (i - 5)**2:
            print(i)
            break
        else:
            print('no')

def q7():
    class A:
        def __init__(self, x):
            self.x = x

        def  __init__(self, o):
            return self.x == o.x

import random
t =[10,20,30,40,50,60,70,80,90]
random=random.choice(t)
print(random)

def pa():
    print("Enter the white house")
    print("i am coming")
print(pa)


def repeat_pa():
    print()
    print()
repeat_pa()

def print_twice():
    print("bruce")
    print("bruce")


print_twice()