#Part 1
import matplotlib.pyplot as plt
import numpy as np
import random
#1
x = np.random.random((5,5))
print"Original:"
print(x)
xmin = x.min()
xmax = x.max()

print 'Minimum and Maximum Values:',xmin, xmax


#2
x = np.random.rand(10, 4)
print(x)
y= x[:5, :]
print'First 5 rows of the above array:',y


#3

x = np.random.random(10)
print'Original:'
print x
x.sort()
print 'Sorted: '
print x

#4

x=np.random.randint(0,10,50)
print 'Original array:'
print (x)
print 'Most frequent value in the above array:'
print np.bincount(x).argmax()

#Question 3


m=1
sigma=2
s=np.radnom.normal(m,sigma,1000)
s=np.random.normal(m, sigma,1000)
m=1
sigma=2
s=np.random.normal(m, sigma,1000)
count, bins, ignored= plt.hist(s,30, normed=True)
plt.plot(bins, 1/(sigma * np.sqrt(2*sigma*2)), linewidth=2, color= 'r')
plt.show()

blah=np.array(np.random.random((99,2)))
plt.scatter(blah[:,0],blah[:,1])
plt.show()

#Question 4
x = [1,2]
y = [[4, 1], [2, 2]]
print np.dot (x, y)
print np.dot(y,x)
print np.inner(x,y)
print np.inner(y,x)


