def printmonth(year,month):
    printmonthtitle(year,month)
    printmonthbody(year,month)

def printmonthtitle(year,month):
    print("     ", getmonthname(month), "     ",year)
    print("--------------------------") 
    print("Sun Mon Tue Wed Thu Fri Sat") 
      