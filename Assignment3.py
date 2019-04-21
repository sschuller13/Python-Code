#Sam Schuller UIN:657353888
#Assignment 3

#Q1
import random

def sim_dice():
    print 'Q1'
    print ' You roll a dice 10,000 times. I dont know why you wasted your time like that,'
    print ' but you did. This is the result of 10,000 rolls'
    print ' '
    var1=0
    var2=var3=var4=var5=var6=var1
    dice={'1':'0', '2':'0', '3':'0', '4':'0', '5':'0', '6':'0'}
    for i in range(0,10000):
        rnd = random.random()
        if rnd <=0.1666666666:
            var1+= 1
            dice.update({'1':var1})
        elif rnd<=0.3333333333:
            var2+= 1
            dice.update({'2':var2})
        elif rnd<=0.5:
            var3+= 1
            dice.update({'3':var3})
        elif rnd<=0.6666666666:
            var4+= 1
            dice.update({'4':var4})
        elif rnd<=0.8333333333:
            var5+= 1
            dice.update({'5':var5})
        elif rnd<=1:
            var6+= 1
            dice.update({'6':var6})
        else:
            print 'Something went wrong'
    print dice
sim_dice()

#Q2
print 'Q2'
print ' '
def sentence_comp(sentence1,sentence2):
    tot=0
    sentence1 = list(set(sentence1.lower()))
    sentence2 = list(set(sentence2.lower()))
    for i in sentence1:
        if i in sentence2:
            tot+=1
    print tot

line1 = raw_input('Enter Sentence 1: ')
line2 = raw_input('Enter Sentence 2: ')

sentence_comp(line1, line2)


#Q3
print 'Q3'
print ' '
def sentence_splitter(sentence, delim1, delim2):
    x1= []

    x=sentence.strip().split(delim1)
    for i in x:
        x2=i.strip().split(delim2)
        for j in x2:
            x1.append(j)
    print x1

inp = raw_input('Input a sentence with a , and /, we will break it up for you')
example= "I like computer programming, including Python , Java, and C/C++"
delim1 = ','
delim2 = '/'
#substitute example until you get the input work
sentence_splitter(inp, delim1, delim2)

            

