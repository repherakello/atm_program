import random
import sys

accountbalan = random.randint(100,10000000)
print('\t\t\tWELCOME TO REPHER@BANK!\n\t\t\tHOW CAN WE HELP YOU TODAY?')
print(' 1.Registration \n 2.Checking Accounts \n 3.Deposit Cash \n 4.Foreign Currency Exchange \n 5.Credit Card')
choice = eval(input('what can we do for you today? 1,2,3.:'))
while choice < 5:
  if choice == 1:
    print("You have choosen to Register with us.Would you like to continue?")
    answer =input("yes / no:")
    if answer == "yes":
        print("thank you for loging in with us")

        id =eval(input("enter your id:"))
        if id in range(1000,3000000):
            print("enter your registration pin:")
            pin =eval(input("enter your pin here:"))
            if pin in range(1000,2000000):
                print("thank you for registaring with us!Would you like to start your saving with us.yes / no")
                yes = answer
               
                no = answer
                eval(input("enter your answer:"))
                if answer == yes:
                   accountblan = random.random()
                   deposit =eval(input("enter amount deposit:ksh"))
                   cash = format(deposit + accountblan)
                   print("your account balance was:ksh",accountblan,"and with the deposit it is now:Ksh",cash)
                   break
                if answer == no:
                   print("Thank you for your registration!") 
                      
                break
            elif pin != range(1000,2000000):
                print("the pin you have entered is wrong try again")
                break
    elif answer == "no":
            print("Thank you for your time.")
            break
            
       


  elif choice == 2:
     print("you have choosen to check on your account balance")
     account =eval(input("enter your accunt number:"))
     if account in range(2000,300000000):
        print("enter your pin")
        pin=eval(input("pin:"))
        if pin in range(1000,200000):
           print("your account balance is:ksh ",accountbalan)
        else:
           print("wrong input!")
     else:
      print("wrong input")
     sys.exit(2)
  elif choice == 3:
    print("you have choosen to Deposit cash on your account")
    account = eval(input("enter your accunt number:"))
    if account in range(2000,300000000):
        print("enter your pin")
        pin=eval(input("pin:"))
        if pin in range(1000,200000):
           deposit =eval(input("enter amount deposit:ksh"))
           money = deposit + accountbalan
           print("your account balance was:ksh",accountbalan,"and with the deposit it is now:Ksh",money)
    else:
       print("wrong input!")
    sys.exit(3)
  elif choice == 4:
    print("you have choosen to exchange your currency to foreign")
  else:
     print("Thank you but the service aint available!")


