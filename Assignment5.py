#Assignment 5
#Week 10
#Sam Schuller

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as so

#1)
def Q1():
    print 'Q1'
    total = 10000
    amount1 = 0
    amount2 = total
    gain = 10250
    while True:
       if amount1 * 1.02 + amount2 * 1.04 == gain:
           break
       amount1 += 1
       amount2 -= 1
       if amount2 == 0:
           break
    print 'Bob invested ', amount1, ' in the first account, and ', amount2, ' in the second'
Q1()


#2) Optimization - Curve Fit (50pts) Given 16 pairs of prices (as dependent variable) and corresponding
#demands (as independent variable), use the curve fitting tool to estimate the best fitting linear,
#exponential, logarithmic, and power curves

print 'Q2'
darray = np.array([3420,3400,3250,3410,3190,3250,2860,2830,3160,2820,2780,2900,2810,2580,2520,2430])
darray = np.asarray(darray, dtype = np.float64)

parray = np.array([127,134,136,139,140,141,148,149,151,154,155,157,159,167,168,171])
parray = np.asarray(parray, dtype = np.float64)

def linreg(darray,a,b):
    return a*darray+b
attributes,variances = so.curve_fit(linreg, darray, parray)
pricemodified = linreg(darray, *attributes)
plt.plot(darray, parray, 'ob', markersize = 2)
plt.plot(darray, pricemodified, '-r', linewidth = 1)
plt.show()

def exponential(darray, a, b, c):
    return a * np.exp(-b * darray) + c

attributes,variances = so.curve_fit(exponential,darray,parray)
pricemodified= exponential(darray, *attributes)
plt.plot(darray,parray, 'ob', markersize = 2)
plt.plot(darray, pricemodified, '-r', linewidth = 1)
plt.show()

def logar(darray, price1,price2):
    return price1 * np.log(darray)+ price2

attributes,variances = so.curve_fit(logar, darray, parray)
pricemodified = logar(darray, *attributes)
plt.plot(darray, parray, 'ob', markersize = 2)
plt.plot(darray, pricemodified, '-r', linewidth = 1)
plt.show()

def powerlaw(darray, a, b):
    return a*(darray**b)

attributes, variances = so.curve_fit(powerlaw, darray, parray)
pricemodified = powerlaw(darray, *attributes)
plt.plot(darray, parray, 'ob',markersize =2 )
plt.plot(darray, pricemodified, '-r', linewidth= 1 )
plt.show()
    



#3)
import numpy as np
import matplotlib.pyplot as plt
from scipy import *
def Q3():
    print 'Q3'
    parray=np.array([127,134,136,139,140,141,148,149,151,154,155,157,159,167,168,171])
    darray=np.array([3420,3400,3250,3410,3190,3250,2860,2830,3160,2820,2780,2900,2810,2580,2520,2430])

    m = (((np.mean(parray)*np.mean(darray)) - np.mean(parray*darray))/((np.mean(parray)*np.mean(parray)) - np.mean(parray*parray)))
    b= np.mean(darray) - m*np.mean(parray)
    print 'Line of best fit is y = ',m,'x  +',b

    plt.plot(parray,darray,".")
    Y=m*parray+b 
    plt.plot(parray,Y) 
    plt.show()

Q3()
#4)
#Q4. Load the data from attached file “Assignment 7_4.csv”. Conduct a clustering algorithm on it. Try out
#  3,4,5 clusters respectively. What do you think is the right number of clusters for this dataset?
from scipy.cluster.vq import *
import pandas as pd
from scipy.cluster.vq import*
from numpy import*
def Q4():
    print 'Q4'
    path = 'C:\Python27\Assignment7_4'
    extra = pd.read_csv(path, header=None)
    extra=df.values
    print extra.shape
    print(pd.value_counts(extra.iloc[:,3:].values.ravel()))
    centroids,_ = kmeans(extra,3)
    index,_ = vq(extra,centroids)
    # some plotting using numpy's logical indexing
    plot(extra[index==0,0],extra[index==0,1],'or',
    extra[index==1,0],extra[index==1,1],'ob',
    extra[index==2,0],extra[index==2,1],'om')
    plot(centroids[:,0],centroids[:,1],'sg',markersize=8)
    plt.show()

    
    centroids,_ = kmeans(extra,4)
    index,_ = vq(extra,centroids)
    # some plotting using numpy's logical indexing
    plot(extra[index==0,0],extra[index==0,1],'or',
    extra[index==1,0],extra[index==1,1],'ob',
    extra[index==2,0],extra[index==2,1],'om',
    extra[index==3,0],extra[index==3,1],'og')
    plot(centroids[:,0],centroids[:,1],'sg',markersize=8)
    plt.show()

    
    centroids,_ = kmeans(extra,5)
    index,_ = vq(extra,centroids)
    # some plotting using numpy's logical indexing
    plot(extra[index==0,0],extra[index==0,1],'or',
    extra[index==1,0],extra[index==1,1],'ob',
    extra[index==2,0],extra[index==2,1],'om',
    extra[index==3,0],extra[index==3,1],'og',
    extra[index==4,0],extra[index==4,1], 'oy')
    plot(centroids[:,0],centroids[:,1],'sg',markersize=8)
    plt.show()


#I pick four clusters because of the distribution, but I'm still having trouble running it consistently   
Q4()



