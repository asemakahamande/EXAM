# the Break statement ends the current loop and jumps to the
# statement immediately following the loop.
# it is like a loop test that can happen anywhere in the body of the loop
while True:
    line= input('>')
    if line == 'done' :
        break
    print(line)
print('Done')

## finishing an Iteration with continue
# the continue statement ends the current iteration and jumps to the top of the loop and starts the next iteration
while True:
     line= input(">")
     if line[0] == '#' :
         continue
     if line == 'done':
         break
     print(line)
print('DOne')

# simple definite loop
for i in [5,4,3,2,1]:
    print(i)
print('Blastoff!')



