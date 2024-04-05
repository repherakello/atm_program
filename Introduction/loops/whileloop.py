password =2345
trial = 0
count = 3

while trial < count:
    pin = eval(input("enter your password: "))
    if pin == password:
        print("You are succesfully logged in:")
        break
    if pin != password:
      print("Wrong pin try again!")
else:
   print("your sim is blocked please contact hotline for help")


    