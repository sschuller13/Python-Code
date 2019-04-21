#Lab Week 3
#1
x= int(input('Type in an integer '))
if x < 100:
      print ('x<100')
elif 100<x<150:
      print "x>100, x<150"
else:
      print "Done"

#2
x=(int(input("Type in an integer(x)")))
if (x%2==0):
      print "Even Number"
else:
      print "Odd Number"

#3
x=(int(input("Type in an integer(x)")))
y=(int(input("Type in an integer(y)")))
if (x<y):
      print "x<y"
elif (x>y):
      print "x>y"
else:
      print ("x=y")

#4
x= int(input('Type in an integer(x)'))
if x<10:
      print ("Good Morning")
elif 10<=x<12:
      print("Almost Lunch Time")
elif 12<=x<18:
      print("Good Day")
elif 18<=x<22:
      print("Good Evening")
else:
      print("Good Night")

#5

Q1= raw_input("Please select your year in school (Freshman, Sophomore, Junior, Senior)")
Q2= int(input("How many courses have you taken so far?"))
if(Q1=='Freshman'):
    if(Q2<=4):
        print ("Take more courses your sophomore year")
    else:
        print("You're taking enough courses for the year")
elif(Q1=='Sophomore'):
    print "You have taken %i courses"%Q2
elif(Q1=='Junior'):
    if(Q2< 12):
        print("Less than 12 courses")
    else:
        print("Keep on keepin on kid")
elif(Q1=='Senior'):
    if(Q2>=16):
        print("You are good to graduate!")
    else:
        print("Sorry you need more courses")
else:
    print("The year you typed is incorrect. Try again")


