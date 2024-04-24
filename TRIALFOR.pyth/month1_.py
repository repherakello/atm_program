def printmonth(year,month):
    print(year,month)

def printmonthtitle(year,month):
    print("printmonthtitle")

def getmonthbody(year,month):
    print("getmonthbody")

def getmonthname(month):
    print("getmonthname")

def getstartday(year, month):
    print("getstartday")

def gettotlanumberofdays(year, month):
    print("gettotalnumberofdays")

def getnumberofdaysinmonth(year,month):
    print("getnumberofdaysinamonth")

def isleapyear(year):
    print("isleapyear")

def main():
    year = eval(input("enter full year(eg 2024): "))
    month = eval(input(("enter month as a number between 1 and 12: ")))

    printmonth(year,month)


main()