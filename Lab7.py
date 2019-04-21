#Lab7

#Q1
#print 'Choose four directions and routes for the robot to travel & the distance traveled will be calculated'
#list=[]
#list2=[]
#for i in range(0,4):
 #   distance=raw_input('Enter the robots direction travel')
  #  steps = int(input('Enter the number of steps the robot takes'))
   # list.append(distance)
   # list2.append(steps)

#for i in range(0,4):
 #   print list[i], list2[i]
#print 'X'

#def distance(list, list2):
    
 #   if list[1]= 'Up' | 'Down'
  #      dY1=list2[1]
   # elif list[1] = 'Left' | 'Right'
    #    dX1=list2[1]

    #if list[2]= 'Up' | 'Down'
    #    dY2=list2[2]
    #elif list[2] = 'Left' | 'Right'
 #       dX2=list2[2]
#
  #  if list[3]= 'Up' | 'Down'
  #      dY3=list2[3]
   # elif list[3] = 'Left' | 'Right'
    #    dX3=list2[3]

    #if list[4]= 'Up' | 'Down'
     #   dY4=list2[4]
    #elif list[4] = 'Left' | 'Right'
     #   dX4=list2[4]


#distance=sqrt()
#print 'The robot travelled',distance

#Q1


#Q2
wordstring= "Beginner means someone who has just gone though an introductory Python course"
wordstring+= "He can solve some problems with 1 or 2 python classes or funtions"
wordstring+= "Normally, the answers could directly to be found in the textbooks"
wordstring+= "Intermediate means someone who ahs just learned python, but already has a relatively strong programming background before"

list_ = wordstring.split()

freq =[]
for w in wordlist:
    freq.append(list_.count(w))
print "String\n"+ wordstring +"\n"
print "List\n" + str(list_) + "\n"



import sys
print sys.path

import csv
with open('C:/Downloads/retail.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        print row
