import sys
def enter_password(username, password):
    if password == 1234 and username.lower() == 'akello':
        return True
    else:
        return False
    

def main():
    username = input("Enter Username")
    password = eval(input("Enter your pin"))
    val = enter_password(username,password)
    print(val)

main()