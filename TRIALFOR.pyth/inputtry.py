def greet():
    """This is a function without parameters that prints hello world"""
    return "Hello world"

# greet()

def greet_person(first_name, last_name):
    return first_name + " " + last_name

def main():
    first_name = input("Enter first name:")
    second_name = input("Enter second name:")
    full_name = greet_person(first_name, second_name)
    print("Hello: {} !!!".format(full_name))

if __name__ == "__main__":
    main()
