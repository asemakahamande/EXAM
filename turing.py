mande = 'God ways are not ours but they are all for good'
d = dict()
for i in mande:
    if i not in d:
        d[i]=1
    else:
        d[i]=d[i] + 1
print(d)


hand={90:"human", "find": 67, "jo":4, "libe":9, "goat":1}
print(hand.get(90))
addr = 'monty@python.org'
uname, domain = addr.split('@')
print(uname)
print(domain)

r = {"mand":  7, " juma":8, "pin": 9, "crown":8}
q=list(r.items())
print(q)
q.sort()

import re
hand = open('my.py')
for line in hand:
    line = line.rstrip()
if re.search('if:', line):
    print(line)

import re
s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\S+@\S+', s)
print(lst)


addr = 'monty@python.org'
uname, domain = addr.split('@')
print(addr)

firstname= 'Mande'
lastname = 'Asemakaha'
fullname=F'hello my first name is {firstname} and my lastname is  {lastname}'

print(fullname)

print('my name is john\n i am from Benue\n i love playing football')

print('''is 
good
from
live''')
print("My name is mande\n i am from Benue\n i love playing football")

