x=5
print 'hello'

def print_oks():
    print "OK1"
    print "OK2"

print "Yo"
x=x+2
print x
print print_oks()
exit

def calc(a,b):
    sum=a+b
    multiply=a*b
    print 'Sum is: ',sum
    print 'Multiplication is: ',multiply

print calc(6,9)
print calc(2.0,9)


def greet(lang):
    if lang == 'es':
        print 'Hola'
    elif lang == 'fr':
        print 'Bonjour'
    else:
        print 'Hello'
greet('en')
greet('fr')
greet('es')


def printinfo(name,age):
    print "Name: ",name
    print "Age: ",age
    return
printinfo("Batman", 35) #orrrrr
printinfo(name="Batman", age=35)
#if you set the function paramter to something in the function declaration, it will become the default argument

# this vartuple represents a list
def printinfo( arg1, *vartuple ):
    "This prints a vairable passed arguments"
    print "Ouput is :"
    print"Arg1: ",arg1
    for var in vartuple:
        print var
    return;
printinfo(10)
printinfo(70,60,50)

#or
#list1=[60,50]
#printinfo(70,list1)# you would need to remove the star before vartuple
#to do this so you're not doing a list of a list

func=lambdaa,b:a+b
func(5,3)
#basically a quick unnamed function
#for lambda functions, you can only use one expression

L=["ccc","b","dd","aaa"]
print "Normal: ",sorted(L)
print("len: ",sorted(L,key=len))
#applying len function to all of the elements here
len('cccc')
L=["cccc","b","ddd","aaa"]
print "Len: ",sorted(L,key=len)
#look at the difference to determine the use of the function



x={1:2,3:4,4:3.2:1,0:0}
x.items()
sorted_by_value=sorted(x.items((), key=lambda kv: kv[1])
#applying the lambda function on top of each one of the tuples in the list
#we're sorting the dictionary based on their values essentially
