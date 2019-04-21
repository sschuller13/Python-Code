import numpy

import numpy as np
from numpy import *
dir(numpy)

x=np.float32(1.0)
print x
y=np.int_([1,2,4])
print y

z=np.arange(3,dtype=np.uint8)
z
z.dtype

print np.array([2,3,1,0])
print np.array([[1,2],[0,0],(1+1j,3.)])

#makes the array full of complex number 


print np.arange(2,3,.1)

import matplotlib.pyplot as plt
x=np.array([.5, .7, 1.0,1.2,1.3,2.1])
bins1=np.array([0,1,2,3])
print(np.histogram(x,bins1))

plt.hist(x,bins=bins1)
plt.show()
