val = format(567895, 'o') #d,0,b,x
print(id(val))
val2 = val
print(id(val2))

tup = [1,2,3,4,5]
tup[0] = 7
print(tup)
greet = "Hello world"
print(greet)



lst = []
for i in greet:
    lst.append(format(ord(i), 'x'))

print(lst)

print("my name is {:.2f}".format(1))