zork = 0
print('Before', zork)
for thing in [9, 41, 12, 3, 74, 15] :
    zork = zork + 1
    print(zork, thing)
print('After', zork)


# summing in a loop
zork = 0
print('Before')
for thing in [9, 41, 12, 3, 74, 15] :
    zork = zork + thing
    print(zork, thing)
print('After', zork)

# finding the average in a loop
count = 0
sum = 0
print('Before', count, sum)
for value in [9, 41, 12, 3, 74, 15] :
    count = count + 1
    sum = sum + value
    print(count,sum,value)
print('After', count, sum, sum/count)

# search using Boolean variable
found  = False
print('Before', found)
for value in [9, 41, 12, 3, 74, 15] :
    if value ==3:
        found= True
    print(found, value)
print('After', found)

# None indicate nothing
smallest = None
print("Before ")
for value in [9, 41, 12, 3, 74, 15]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest= value
    print(smallest, value)
print('After', smallest)