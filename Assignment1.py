#Sam Schuller UIN:657353888
#1.1
#!/usr/bin/python p
print'Question 1'
x = 0
y = 3
for i in range(1, y + 1):
    for space in range(1, (y - i) + 1):
        print '  ',
    while x != (2 * i - 1):
        print '* ',
        x = x + 1
    x = 0
    print '\r'

#1.2
import math
from math import sqrt
print 'Question 2'
print "Equation= x^2 - 40x + 391"
A = float(input("A: "))
B = float(input("B: "))
C = float(input("C: "))
N = B**2 - 4*A*C
print "Square rt of N is ", math.sqrt(N)
no1 = (((-B) + sqrt(N))/(2*A))
no2 = (((-B) - sqrt(N))/(2*A))
print "The two roots: %f and %f" % (no1, no2)

#1.3
print 'Question 3' 
integers = raw_input("Insert your two numbers after this:")
x = int(input("Enter x~ "))
y = int(input("Enter y~ "))
print '(x+y)/(x-y) = ', int((x+y)/(x-y))
print '(x-y)^3 = ', int((x-y)*(x-y)*(x-y))
equation = (x+y)
print 'x+y =', int(equation)
print 'The last digit of x+y:', (str(x+y)[-1])

#1.4
print 'Question 4'
#Rock is 1
#Paper is 2
#Scissors is 3
wins=0   
wins2=0    
ties=0    

y = "Make the ultimate choice: Rock, Paper or Scissors?"
print y    
x = input('Player 1: 1 is Rock, 2 is Paper, 3 is Scissors : ')
choice = x    
blah= input('Player 2: 1 is Rock, 2 is Paper, 3 is Scissors: ')
choice2 = blah
if (choice, choice2) == (1, 2):    
  wins2 += 1    
  print 'Player 2 wins, they chose paper, Player 1 chose rock.'
elif (choice, choice2) == (3, 2):    
  print 'Player 1 wins, they chose Scissors, Player 2 chose paper'    
  wins += 1    
elif (choice, choice2) == (2, 2):    
  print 'TIE! You both chose paper.'    
  ties += 1    
elif (choice, choice2) == (1, 3):    
  print 'Player 1 Wins, they chose rock & Player 2 chose scissors'    
  wins += 1    
elif (choice, choice2) == (3, 3):   
  print 'TIE! You both chose scissors'    
  ties += 1    
elif (choice, choice2) == (2, 3):    
  print 'Player 2 wins, they chose scissors, Player 1 chose paper'    
  wins2 += 1    
elif (choice, choice2) == (1, 1):    
  print 'TIE! You both chose rock'    
  ties += 1    
elif (choice, choice2) == (3, 1):    
  print 'Player 2 wins, they chose rock & Player 1 chose scissors'       
  wins2 += 1    
elif (choice, choice2) == (2, 1):    
  print 'Player 1 wins, they chose paper & Player 2 chose rock'       
  wins += 1    
else:
  print 'Please choose between 1, 2, or 3 otherwise this won\'t work'
if(choice) >3:
    print 'Player 1 don\'t do that'
elif(choice2)>3:
    print 'Player 2 dont\'t do that'
elif(choice)<0:
    print 'Player 1 don\'t do that'
elif(choice2)<0:
    print 'Player 2 don\'t do that'
print 'Game Over'

if wins==1:
  print 'PLAYER 1 WON'      
elif wins2==1:    
 print 'PLAYER 2 WON'    
else:
    print 'You tied. Thats pretty anticlimatic'
    
#1.5
print 'Question 5'
temp=int(input("Please enter a temperature:"))
unit=raw_input("Is this Celsius(C) or Fahrenheit(F)?")
if(unit=="C"):
    answer = ((temp*9/5)+32)
    print answer
    print "%iC is %i in Fahrenheit "%(temp,answer)

elif(unit=="F"):
     answer = ((temp-32)*5/9)
     print answer
     print "%iF is %i in Celsius "%(temp,answer)
else:
    Print("Invalid temperature unit entry, enter C or F next time")
