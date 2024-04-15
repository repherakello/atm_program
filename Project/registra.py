def registration_point():
    print("how can we help you")
    for _ in range(7):
            choice = eval(input("please enter your answer.1,2,3,4...:"))
            if choice not in [1,2,3,4,]:
                print("invalid input. please enter 1,2,3,4,5....")
            else:
                break   
    while choice < 5:
        if choice == 1:
         print("You have choosen to Register with us.Would you like to continue?")
         for _ in range(7):
            answer = input("please enter your answer.yes / no:")
            if answer not in ["yes","no"]:
                print("invalid input. please enter 'yes' or 'no'.")
            else:
                break    


        if answer == "yes":
            for id in range(3):
                id =eval(input("enter your id:"))
                if id not in range(1000,3000000):
                    print("Wrong input try again!")
                else:
                    break 
                   
            for pin in range(3):        
                pin =eval(input("enter your pin here:"))
                if pin not in range(1000,2000000):
                    print("wrong input try again!")
                else:
                    break    
                print("thank you for registaring with us!Would you like to start your saving with us.yes / no")
                
            decision =eval(input("enter your answer:"))

            if decision not in ["yes","no"]:
                print("wrong input try again")
                for decision in range(3):
                    return registration_point(choice)
                if decision== "yes": 
                   accountblan = random.random()
                   deposit =eval(input("enter amount deposit:ksh"))
                   cash = format(deposit + accountblan)
                   print("your account balance was:ksh",accountblan,"and with the deposit it is now:Ksh",cash)
                    
                elif decision == "no":
                   print("Thank you for your registration!") 
                      
                   break
            elif pin != range(1000,2000000):
                print("the pin you have entered is wrong try again")
                break
        elif answer == "no":
            print("Thank you for your time.")
            break
registration_point()       