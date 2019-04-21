#Sam Schuller
#UIN: 657353888


#Q1
x=0
print x
while x<10:
    x=x+1
    print x
    
#Q2
A="**********"
x=10
while x>0:
    print A[1:x]
    x=x-1
    
    
#Q3
n=10
for i in range(n):
    print(' '*(n-i-1) + '*'*(2*i+1))
 

#Q4
for i in range(n):
    print(' '*(n-i-1) + '*'*(2*i+1))
b=10
for i in reversed(range(b)):
    print(' '*(b-i-1) + '*'*(2*i+1))
#Q5


#Q6
import random
cpu = random.randint(0,1000)
print 'Whats the CPUs secret number??'
guess =int(input("Enter a value between 1-1000 to guess the Cpu's number"))
while cpu != guess:
    if guess > cpu:
        print 'The Cpu has a lower number than that, try again'
    elif guess < cpu:
        print 'The Cpu has a higher number than that, try again'
    guess =int(input("Enter a value between 1-1000 to guess the Cpu's number"))

print'You did it! good guess'

