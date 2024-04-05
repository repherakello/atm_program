n = 5
for i in range(n):
    for j in range(n):
        print("*", end="")

#increasing triangle
l = 5
for k in range(l - 1):
    for t in range(k ):
        print('*',end = "") 
    print()  

k = 7-1
for y in range(k):
    for u in range(y - 1):
      print("@", end = "")
    print()    

    #hill pattern
n = 5
for i in range(n):
    for j in range(i,n):
        print("",end ="")
    for j in range(i):
        print("*",end = "")
    for j in range(i +1):
        print("*",end ="")
    print()


n = 5
for i in range(n):
    for j in range(i,n):
        print("",end="")
    for j in range(i):
        print("*",end="")
    for j in range(i -1):
        print("*",end ="")
    print(  )
    
for i in range(n):
    for j in range(i,n):
       print("",end="")
    for j in range(i,n-1):
        print("*",end="")
    for j in range(i,n):
        print("*",end="")
    print()
    
#right triangle
for i  in range(n):
    for j in range(i +1):
        print("*",end="")
    for j in range(i,n):
        print("",end="")
    print()
for i in range(n):
    for j in range(n):
        print("",end="")
    for j in range(i):
        print("*",end ="")
    for j in range(i,n +1):
        print("*",end ="")
    print()