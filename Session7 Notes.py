s = 'spam'
e = 'eggs'

print 3*s
print s+e+s+e


s.find('s')
s.count("spam")

s= 'Joker'
list1=['Batman','Superman']
print s.join(list1)

fh=open('ionosphere.txt','r')
inp=fh.read()
print len(inp)
print inp[:20]
lines = fh.readlines()
print lines[:2]

