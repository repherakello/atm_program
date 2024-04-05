import base64
"""
#Mathematical operators
 - Addition +
 - Subtraction -
 - Multiplication *
 - Division /
 - Modulus %

 #Comparison Operators - Comparison Operators return a true of false response
  - greater than >
  - less than <
  - equal to ==
  - greater than or equal to >=
  - less than or equal to <=

  #Logical Operators
  Logical and - and &&
  Logical or - or ||
  Logical not - not !=
  logical XOR -  ^
"""


num1 = 10
num2 = 5
num3 = 15

result = num1 > num2
print("Greater than: ", result)

result = num1 < num2
print("Less than: ", result)

result = num1 == num2
print("equal to: ", result)


if num1 >= num2 and not num2 >= num3:
    print("Am greater", "\u1F60")


ch = 'a'
print(format(ord(ch),"b"))

message = "Hello world"

encd = base64.b64encode(message.encode())
print(encd)
decd = base64.b64decode(encd)
print(decd.decode())