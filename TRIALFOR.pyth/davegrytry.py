"""def gin_no():
    x = 3
    p = 4
    p >= x
    great = p
    print("the greatest between",x,p,"and",great,"is:")

 
gin_no()"""
def multiply():
    print("\t\t\t MULTIPLICATION TABLE \t\t\t")

print("  |",end=" ")
for j in range(1 , 10):
    print(" ",j,end = "  ")
print( )
print("----------------------------------------------")   


for i in range(1 , 10):
    print(i,"|", end = "")
    for j in range(1,10):
        print(format(i * j, "4d"),end =" ")
    print()    

multiply()   