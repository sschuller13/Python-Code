#Sam Schuller
#Assignment4.1
#Q1

import Assignment4 #imports assignment4 file w two methods

print '4+3 = '
print Assignment4.add(4,3) #prints the result of addition between these two numbers
print 'Fool'
print Assignment4.get_length("Fool") #prints the total characters in the String provided here


import os


#Q2   
def Q2():
    # Show directory in the console
    print 'The current directory: ',os.getcwd()
    # Shows the files this directory
    print ' The files in this directory are: ',os.listdir('C:\Users\s_sch\Desktop\pythonAssign4')
    print''
    diction = {} #empty dictionary
    inp = input('Enter the file directory: ')
    #try-catch block
    try:
   	 os.chdir(inp)     # Accesses directory user chooses
   	 inp = input('Enter the file name: ')    # Finds file in directory
    except: pass   #if the directory isn't there it moves on
    x1 = inp
    file = open(x1,'r').read()  #Reads file
    print ' '
    print ' '
    file = file.replace(',',' ').replace('.',' ').replace('!',' ').replace(':',' ').replace('?',' ').replace('(',' ').replace(')',' ').replace('-',' ').lower()
    data = file.split()
    for i in data:
   	 try: diction[i] += 1    # Repeated words will add a value to dictionary
   	 except: diction[i] = 1 # Adds words
    for j in sorted(diction.keys()): print ('%-12s: %-12d' % (j, diction[j]))    # Prints out ordered dictioneary
    return null
print Q2()

#Q3
def Q3(x):
    fh = open(x,'r').readlines() #reads file
    stripper = [i.strip() for i in fh] #strips file
    splitter = [i.split(',') for i in stripper] #splits file
    diction = {}#empty dictionary
    opener = open_file('retail.csv')
    for row in opener:
   	 for i in range(1,3): 
             #try catch block
   	     try: diction[row[i]] += 1    # Repeated words will add a value to dictionary
   	     except: diction[row[i]] = 1    # Adds words
    for j in sorted(diction.keys()):
        print ('%-12s: %-12d' % (j, diction[j]))
    return null
Q3('retail.csv')
