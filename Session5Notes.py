#Week 5 2/14/19

x= range(3,6)
sum=0.0
for i in x:
    sum+=i
avg=sum/len(x)
print "Average is: ", avg

a=[9,41,12,3,77,19]
print a
a[1:3]=[]
print a

a=list()
print a

a.append('book')
print a
a.append('30')
print a

a.append([3,'james'])
print a #3 elements now, makes the whole list ONE element

b=['book',30]
print b+[3,'james'] #notice difference between + and append

a=[3,1,10]
sorted(a) #this just creates a new list
print a 
a.sort() #this sorts but doesn't save it like this, if you did a[1] you'd still get 3
print a


numList=list()
while True:
    inp=raw_input('Enter a number:')
    if inp=='done':
        break
    value=float(inp)
    numList.append(value)
print numList

tuple1=['a','b',1]
print tuple1

#immutable, elements unchangable

#tuple=('a',) allows it to be a tuple, if you dont put the comma it'll just be a string
a,b,=(1,7)
a
b
a,b=b,a


eng2sp = {}
eng2sp['one'] = 'uno'
eng2sp['two'] = 'dos'
print eng2sp
{'one':'uno','two':'dos'}


counts=dict()
names=['csev','cwen','csev','zquian','cwen']
for name in names:
    counts[name]=counts.get(name,0)+1
#name is the iteration, names is the name of the list, and this counts the number of times each names appears in the given dictionary
print counts

