def f(w = 1, m = 2):
    print(w,m)


f()
f(w = 4)
f(m =34)
f(3,6)
 

def main():
    nprintin(5)

def nprintin(message ="welcome home", n =1):
    for i in range(n):
        print(message)
    
main()


def sort(number1,number2):
    if number1 < number2:
        return number1, number2
    else:
        return number2, number1

n1,n2 = sort(9,7)
print("n1 is",n1)
print("n2 is",n2)


"""
does it mean that when we use return it isn't a big deal
when you do not call the function again but instead print
"""


def h(j,k):
    return j + k, j * k, j // k, j % k, j / k

t1,t2,t3,t4,t5 = h(7,2)
print(t1,t2,t3,t4,t5)

h(10,4)







