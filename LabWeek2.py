
x=3
y=5
z=2.5
m='2.7'
print(x+y)
print(x/y)
type(m)
jsf=float(m)
print jsf+y
#Q3
x=raw_input("Operand 1?")
y=raw_input ("Operand 2?")
x1=int(x)
y1=int(y)
print x1+y1
print x1/y1

#Q4
print('Here is Q4')
print(20+10)
print(7/3)
print(7//3)
print(7%3)

#Q5
print('Here is Q5')
a=10
print (a)
b=7
print (b)
print (a+b, "Addition")
print (a-b, "Subtraction")
print (a*b, "Multiply")
print (a/b, "Divide")
print (a%b, "Modulo")


#Q6
print('Here is Q6')
print (a>b)
print(a == b)
print (a != b)


#Q7
print('Here is Q7')
print(a>=b & a>5)
print(a<=b & a>5)
print(not a)

#Q8
a=10
b=5
print('Here is Q8')
print(a+b>15 | a-b<8)
print(a+b>15 | (a-b<8 & False))
print(a+b>15-2*2**4/4 & (not False))

#Q9
user=raw_input("Enter an integer w more than two digits")
print("Here are the final two digits of said number")
print user[-1:2]
print '%02d' % (user%100)
