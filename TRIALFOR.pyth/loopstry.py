#we have two types of loops:
#.01.while loop
#example 1.
import random


we = 0
while we < 10:
    print("we are two")
    we =we + 1

numb1 = random.randint(1 , 19)
numb2 = random.randint(1 , 19)

if numb1 < numb2:
   numb1,numb2 = numb2,numb1

answer= eval(input("what isthe sum of" + str(numb1) + "+" +str(numb2) +"="))
while numb1 + numb2 != answer:
    answer=eval(input('wrong answer.try again'+ str(numb1) +"+"+ str(numb2) +"="))
print("you are correct!")


number = random.randint(0 , 100)
guess = number


for digit in range(0,3):
  print("enter a guess:")
  num =eval(input())
  if num == number:
    print("correct guess")
    if num != number:
       print("wrong input,try again!")

    

