while True:
    line = input('> ')
    if line [0]=="#":
        continue
    if line == 'done':
        break
    print(line)
print('Done!')


#for loop
fruits = ['Banana', 'Apple', 'Guava', 'orange', 'grape']
for fruit in fruits:
    print('I love this fruit', fruit)
x = 7
x = 9
print(x)

count= 0
for itervar in [3, 41, 12, 9, 74, 15]:
    count= count + 1
print('count:', count)
print(itervar + 4)

total = 0
for itervar in [3, 41, 12, 9, 74, 15]:
    total = total + itervar
#print(itervar + 4)
print('Total: ', total)

list = [1, 2, 3, 4, 5, 6]
for li in list:
    print(li + 4)