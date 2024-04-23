from random import randint
getRandomCharacter = ""

def getRandomCharacter(ch1,ch2):
    return chr(randint(ord(ch1),ord(ch2)))

def getRandomLowerCaseletter():
    return getRandomCharacter('a','z')

def getrandomuppercaseletter():
    return getRandomCharacter("A","Z")

def getrandomdigitcharacter():
    return getRandomCharacter("0","9")

def getrandomASCIIcharacter():
    return chr(randint(0, 127))

    

 