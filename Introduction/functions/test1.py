import sys


def greet_user(username: str):
    """
    This is a function that takes a username and prints out a greeting to the console,
    """
    return f"Hello,{username}"

# name = input("Enter your name: ")
# greet_user(name)
is_logged_in = False
def pin_entry():
    sim_pin = 1234
    pin = eval(input("Enter your pin"))
    if pin == sim_pin:
        print("Correct entry granted")
        is_logged_in = True
        return is_logged_in
    else:
        print("Wrong pin try again")

def something():
    allowed = True
    attempts = 0
    while allowed:
        while attempts < 3:
            pin_entry()
            attempts += 1
        print("Sorry sim blocked")
        allowed = False
def main():
    if is_logged_in == False:
        something()
    else:
        pass
main()
