#Lab5

#Part1
print 'Part 1'
print ' '
sentence=raw_input("Enter a sentence here")
x=0
y={}
for i in sentence:
    if (i == ' '):
        continue
    y[i] = x
for j in sentence:
    for k in y.keys():
        if j==k:
            y[k]+=1
print y
print ' '


#Part2
print ' '
operation=raw_input("please select operation: (1: sort by key, 2: sort by value)")
dictionary={'x':7, 'y':2, 'a':3, 'm':2}
if operation=='1':
    for i in sorted(dictionary.iterkeys()):
        print "%s, %s"%(i, dictionary[i])
elif operation == '2':
    for i, value in sorted(dictionary.iteritems(), i=lambda (i,v): (v,i)):
        print " ",i ," %s"%( value)
print ' '
