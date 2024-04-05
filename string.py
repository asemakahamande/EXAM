cars = list(("honda", "toyota"))
print(type(cars))

a= ['a', 'b', 'c']
b = list(('d', 'e'))
#a.extend(b)
b.extend(a)
print(a)
print(b)
a.append(b)
print(a)

point = input("Enter points:")
print(point)


t = ['pining', 'for', 'the', 'fjords']
delimiter = ' '
print(delimiter.join(t))