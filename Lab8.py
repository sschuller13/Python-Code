#Lab 8
#Sam Schuller
#Question 1
 def open(name):
   	 file = open(name,'r').readlines()
   	 file_strip = [s.strip() for s in file]
   	 file_split = [s.split(',') for s in file_strip]
   	 return file_split
    def q1_1(stuff):

         mBalance = 0.0;    wBalance = 0.0
   	 mCount = 0;    wCount = 0
   	 for a in stuff:
   		 if 'Male' in a:
   			 mBalance = mBalance + float(a[len(a)-1])
   			 mCount = mCount + 1
   		 else:
   			 wBalance = wBalance + float(a[len(a)-1])
   			 wCount = wCount + 1
   	 #print ("Total Males: ", mCount)
   	 #print ("Total Females: ", wCount)
   	 print ("Average Male Balance is: ", mBalance/mCount)
         print ("Average Female Balance is: ", wBalance/wCount)
   	 return 0

    def q1_2(stuff):
         wBalance = 0.0; bBalance = 0.0
   	 white = 0; blue = 0
   	 for b in stuff:
   		 if 'England' in b:
   			 if 'White Collar' in b:
   				 wBalance = wBalance + float(b[len(b)-1])
   				 white = white + 1
   			 elif 'Blue Collar' in b:
   				 bBalance = bBalance + float(b[len(b)-1])
   				 blue = blue + 1
   			 else: pass
   	 print ("Average While Collar Balance is: ", wBalance/white)
   	 print ("Average Blue Collar Balance is: ", bBalance/blue)
   	 return 0    
    def ex1():
   	 stuff = Lab8.open_file('customer-savings.txt')
   	 Lab8.ex1a(stuff); print()
   	 Lab8.ex1b(stuff)
