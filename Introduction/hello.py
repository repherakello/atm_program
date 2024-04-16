# scopes where you use globa to change value of the global variables
name = input("enter your name: ")
name2 =input("enter your second name:")

def MY_NAME():
    """
    this function takes the name of the user and display on the console
    """
    
   
 
    global x
    name = "akello"
    name2 = "repher"
    for count in range(3):
        if name == 'akello' and name2 == 'repher':
            print("My name is",name,name2)
            break
        elif name != 'akello' and name2 == 'repher':
            print('input',name,'wrong but',name2,'correct')
            return count

        else:
             print('wrong input:') 
             break
           
MY_NAME() 
