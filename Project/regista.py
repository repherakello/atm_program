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

        """
if the user provides correct input, as yes then the programme should execute to ask user to add the id
what if the user adds the id as a string?what if the user sums different types of data types?
the programme should not fail if any of this take place at any point of id or pin insertion...

    """
        if answer == "yes":
            count = 0
            while count < 3:
                id =eval(input("enter your id:"))
                if id in range(1000,3000000):
                    print("succesfull addition of id:")
                    break
                if id not in range(1000,3000000):
                    print("Wrong input try again!")
                    count +=1    
                else:
                    break 
                   
        if id == range(1000,3000000):           
            while count < 3:       
                pin =eval(input("enter your pin here:"))
                if pin in range(1000,2000000):
                    for count in range(2):
                        print("add the pin you used the second time for confirmation.")
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