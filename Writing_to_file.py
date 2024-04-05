mande = open('man.txt', 'w')
line1 = 'God will help us all. \n'
mande.write(line1)
line2 = "I am a Man u fan"
mande.write(line2)
mande.close()

h=open('man.txt','r')
print(h.read())
