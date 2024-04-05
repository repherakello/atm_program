"""import random
print("wELCOME TO REPHER@TEACHING!",)

number1 = random.randrange(0, 10)
number2 = random.randrange(0, 10)

if number1 < number2:
    number1,number2 = number2,number1


    answer =eval(input('what is' +str(number1)+'-' + str(number2) +'?'))

    if number1 - number2 == answer:
        print('you are correct!')
    else:
        print('your answeris wrong.\n',number1,'-', number2,'is',number1 -number2,'.')"""





#loops
 #this print it 100 times releasing the tiresome coding to 101 times       
"""count =0
while count < 100:this means that it must be greater than 99 for it to be false and stop printing 
    print("programming is fun!")
    count = count + 1"""

"""number3 = random.randint(0,200)
number4 = random.randint(0,200)

if number3 > number4
number3,number4 = number4,number3

answer=eval(input("what is"+str(number1)+"+"+str(number2)+"?"))
print(number3,"+"number4,"=",answer,"is"number3+number4== answer)"""

"""
day = 0
question1 ="is your birthday in set?\n"+\
"1 3 5 7 \n"+\
"9 11 13 15 \n"+\
"17 19 21 23 \n"+\
"25 27 29 31"+\
"\n Enter 0 for No and 1 for Yes:"
answer = eval(input(question1))
if answer == 1:
  day += 1

question2 ="is your birthday in set 2?\n"+\
"2 3 6 7\n"+\
"10 11 14 15\n"+\
"18 19 22 23\n"+\
"26 27 30 31"+\
"\n Enter 0 for No and 1 for Yes:"
answer=eval(input(question2))
if answer == 1:

  day +=2

question3 ="is your birthday in set3?\n"+\
"4 5 6 7\n"+\
"12 13 14 15\n"+\
"20 21 22 23\n"+\
"28 29 30 31"+\
"\n Enter 0 for No and 1 for Yes:"
answer =eval(input(question3))
if answer == 1:

    day +=4

question4 ="is your birthday in set4?\n"+\
"8 9 10 11\n"+\
"12 13 14 15\n"+\
"24 25 26 27\n"+\
"28 29 30 31"+\
"\n Enter 0 for No and 1 for Yes:"
answer =eval(input(question4))
if answer ==1:
   day +=8

question5 ="is your birthday in set 5?\n"+\
"16 17 18 19 \n"+\
"20 21 22 23 \n"+\
"24 25 26 27 \n"+\
"28 29 30 31"+\
"\n Enter 0 for No and 1 for Yes:"

answer =eval(input(question5))
if answer ==1:
   day +=16

   print("\n your birthday is"+ str(day)+"!")
"""


for i in range(1,4):
    for j in range(1,4):
        if i * j> 2:
            break
        print(i * j)
    print(i)


    for i in range(1,4):
        for j in range(1,4):
            if i * j > 2:
                continue
            print(i * j)
        print(i)