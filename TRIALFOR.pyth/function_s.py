def trial():
    print("hello world!")
def count(num1,num2):
    if num1 > num2 :
        result = num1
    else:
        result =num2

    return result
def gcd(numb1,numb2):
    gcd = 1
    m =2
    while m <= numb1 and m<= numb2:
        if numb1 % m == 0 and numb2 % m == 0:
            gcd = m
        m +=1
    return gcd

def main():
    
    j = 4
    k = 3
    i = count(4,3)
    print("the largest number in",j ,"and",k,"is",i)
   

main()
trial()
