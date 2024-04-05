#creating the pin Blocker

import random
import time

 

correctcount = 0
count = 0
number_try = 3
starttime =time.time()
while count< number_try:
    pin = 2345
    pin2 = random.randint(10 , 4567)
    pin != pin2 

    answer=eval(input("enter your secret pin"))

    if answer == 2345:
       print("you are logged in ,Thank you")
       break
    else: 
       print("try again!",)
       count +=1
    if count == 3:
       print("your  sim is blocked")
       
    endtime =time.time()
    timetaken= int(endtime - starttime)
    print("time taken is",timetaken,"seconds")
    
       
