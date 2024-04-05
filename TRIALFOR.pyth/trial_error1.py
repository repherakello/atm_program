import random

print("Welcome To My Trial Program for Python")
#Simple Calculating the area of things
#1.Circle
PI = 3.142
radius=eval(input("Add the radius of  the circle:"))
area=radius ** 2 * PI 
if radius <= 0:
    print("wrong input try again!")
    if radius <= 0:
        print("Wrong input please try again")
elif radius >= 100000:
    print("Larger input and cannot be solved!")
else:
    print("the area of the circle of radius:{:.2f} is: {:.2f}".format(radius,area))


#try area by the use of Random.randint,randrange....
radius = random.randint(0,99)
area1=eval(input("enter your guess (2radius):"))

guessradius1 = radius // 10
guessradius2 = radius % 10

area1guess1 = area1 // 10
area1guess2 = area % 10

print("The radius is",radius)

if area1 == radius:
    print("you have entered the correct guess",area1,"And succesfully won $5000")
elif (area1guess2 == guessradius1 and 
    area1guess1 == guessradius2):
    print('match the digits for radius well and win $3000')
elif ( area1guess1==guessradius1
      or area1guess2 == guessradius1
      or area1guess1 ==guessradius2
      or  area1guess2==guessradius2):
    print("guess one digit and stand a chance to win $1000")
else:
    print("you lost the chance")