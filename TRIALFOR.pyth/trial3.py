import time

#numb1,numb2,numb3 = input("enter three numbers separeted with a coma:").split(",")
#print(numb1,numb2,numb3)

intnumb1 = 2
boolnumb2 = int("03")
#Note that string dosnt take eval when theirs a leading 0 like above example and therefore it returns an error.
#it only takes an int
answer= intnumb1 ** boolnumb2

print(f"{answer:.2f}")

currenttime = time.time()
totalsecond = int(currenttime)
currentsecond = totalsecond % 60
totalminute = totalsecond // 60
currentminute = totalminute % 60
totalhours = totalminute // 60
currenthour = totalhours % 24
print("current hour 2024,march,23 is",currenthour,".",currentminute,".",currentsecond,"EAT")


elit =chr(500)
print(elit)
print("he said\"My programme is easy to read\"")


