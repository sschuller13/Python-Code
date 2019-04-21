#Sam Schuller UIN:657353888
#Assignment 2

#2.1
print 'Q1'
print ' '
print ' '
n = int(input('Enter a positive integer (n)'))
if(n>0):
    place=0
    while n>0:
        place=place+(2*n-1)
        n-=1
    print'Here is the sum of all odd numbers up to 2n-1: ',place
else:
    print 'The input you have is not valid. It must be positive'
print ' '


#2.2
print 'Q2'
print ' '
print ' '
n = int(input('Enter a positive integer(n)'))
for a in range(1, n+1):
    for b in range(1, a+1):
        print b,
    print("")
print ' '

#2.3
print 'Q3'
print ' '
print ' '
def leibniz(n):
    denom = 1.0
    plus = 1.0
    for i in range(0,n):
        denom = denom + 2
        plus = plus - (1/denom)
        denom = denom + 2
        plus = plus + (1/denom)
    x = plus * 4
    return x

print 'Value of n is 1,000,000. In the Leibniz Formula that equates to Pi = : '
print leibniz(1000000)
print ' '

#2.4
print 'Q4'
print ' '
print ' '
marbles= int(input('Enter the total number of marbles'))

while(marbles>0):
    print 'Player 1'
    print 'How many marbles do you choose?' 
    print '1, 2, or 3'
    play1 = int(input(">"))
    print 
    if play1 < 4 and play1 > 0: 
        marbles = marbles - play1  
        print 'Player 1 takes', play1, " marbles, there's now ", marbles, "marbles"
        if marbles > 0:
            print 'Player 2'
            print 'How many marbles do you choose?' 
            print '1, 2, or 3'
            play2 = int(input(">"))
            if (play2 < 4 and play2 > 0):
                marbles = marbles - play2 
                print 'Player 2 takes', play2, " marbles. theres now ", marbles, "marbles"
                if (marbles<= 0):
                    print '0 Marbles left, Player 2 wins'
            else:
                print'You cant pick more than 3 marbles. Now you lose your turn.'
        else: 
            print "0 marbles left, Player 1 wins"                  
    else: 
        print 'You cant pick more than 3 marbles. Now you lose your turn'

print ' '
#2.5
print 'Q5'
print ' '
print ' '
r=int(input("Enter an integer for your super triangle"))
i = 1
if(r>0 and r<=10):
    while i < r + 1:
        j=0
        while j < i:
            print "*",
            for j in range(1,2*i-1):
                print "*",
            for y in range(1,4*((r-i)+1)):
                print " ",
            for z in range(1,2*i):
                print "*",
            j+=1
            print
        i+=1
else:
    print 'Im gonna be honest. Any number more than 10 will break it. It starts overlapping'
    print 'If you tried to print 0 or less than 0 youre just being rude'

