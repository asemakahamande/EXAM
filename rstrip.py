#mande = open("fan.txt", "w")
#line1 = "I will serve God with Python.\n"
#fine = mande.write(line1)
#line2 = "God you are my Father, I have no other god but YOU "
#finee = mande.write(line2)
#mande.close()

#print(finee)
#jet = open("fan.txt","r")
#print(jet.read())
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File does exist in this directory:', fname)
    exit()
count = 0
for line in fhand:
    if line.startswith('What'):
        count = count + 1
print('There were', count, 'What lines in', fname)

