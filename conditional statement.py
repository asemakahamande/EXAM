score = 71
if score >=80:
    print("A")
elif score >=70:
    print("B")
    if score ==71:
        print("upper B")
    elif score ==78:
        print("excellent B")
    else:
        print("normal score")
elif score >=60:
    print("c")
else:
    if score >=50:
        print("F you will repeat")
    elif score >=40:
        print("go to your father's house")
    else:
        print("Don't come with your father")


# for functions
even_Numbers = 2.9, 4.5, 6.7, 8.6, 10.9
print(len(even_Numbers))
print(len("Hello world"))

print(type(even_Numbers))
print(int("32").bit_length())
print(12/7)
help("pass")

print(float(3))
import math
print(math)
tan = 89
print(math.sin(tan))
import random
t = [1,2,3]
print(random.choice(t))



def my_name():
    print("my name is mande")
#my_name()

def sur_name():
    print("my sur name is Asemakaha and  ")
    my_name()
sur_name()


def adding_numbers():
    a=4
    b=7
    c=a+b
    print(c)
    print("the answer is 11")
    sur_name()

adding_numbers()

fruits = ['grape', 'apple', 'mango', 'orange']
for k in fruits:
    print(k)


def print_twice(John):
    print('John')
    print('John')




while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('Done!')


while True:
    a = input("enter value of a:")
    b = input(" enter value of b:")
    if a == b:
        break
    print(a)
print("free to go")

while True:
    line=input('>')
    if line[0]=="T":
        continue
    if line == "done":
        break
    print(line)
print('done')


states = ['Benue', 'FCT', 'Kogi', 'kebbi', 'Lagos']
for state in states:
    print("I love my state:", state)
print("done")