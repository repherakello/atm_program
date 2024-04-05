import random
import string

prefix = "QSM"
randval1 = "".join(random.choices(string.ascii_uppercase + string.digits, k=8))
print(randval1)
randval2 = prefix +randval1
print(randval2)