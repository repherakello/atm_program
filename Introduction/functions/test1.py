def enter_password(pin):
    if pin == 1234:
        print(1)
        return True
    else:
        print(1)
        return False

def login_user():
    attempts = 0

    while attempts < 3:
        pin = eval(input("Enter your pin"))
        val = enter_password(pin)
        if val:
            print("User logged in Succesfully")
            break
        else:
            print("Incorrect password Enter again")

        attempts += 1

    print(2)

    return val

def main():
    is_logged_in = login_user()
    print(is_logged_in)
    if is_logged_in:
        print("Menu")
    else:
        print("Too many attempts account locked")

    print(3)

main()