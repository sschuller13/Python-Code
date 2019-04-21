myDict = {'id': '1001', 'name': 'alice', 'age': '20'}
for k in myDict.keys():
    print myDict[k]

    
nums = range(10)
i = 0
while i < len(nums):
    print nums[i]	# (S1)
    i += 1	# (S2)
    print i

stars = 5
width = stars*2
for i in range(5):
    s = (i+1)* '*'
    s += (stars - (i + 1))*2* '-'
    s += (i+1)* '*'
    print s

nums = range(10)
i = 0
while i < len(nums):
    print nums[i]	# (S1)
    i += 1	# (S2)	
print i
nums = range(10, 20)
for i in range(10):
    if i%2 == 0:
        print nums[i]
    else:
        if i == 5:
            break
 
        else:
            print nums[i]*2

print nums


stars = 5
width = stars*2
for i in range(5):
    s = (i+1)* '*'
    s += (stars - (i + 1))*2* ' '
    s += (i+1)* '*'
    print s

pyramid = 8
for i in range(0,pyramid):
    string = '*'
    string+=(pyramid-i)* ' '
    print string
    string+='*'
