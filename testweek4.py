x=5
while x>3:
    print x
    x  = x-1
print x+1


while True:
    line = raw_input('>')
    if line == 'done':
        break
    print line
print 'Done!'
