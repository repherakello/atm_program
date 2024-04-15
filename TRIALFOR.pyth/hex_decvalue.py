def decimalToHex(decimalvalue):
    hex = " "
    while decimalvalue != 0:
        hexvalue =decimalvalue % 16
        hex = toHexchar(hexvalue) + hex
        decimalvalue = decimalvalue // 16

    return hex    

def toHexchar(hexvalue):
    if 0 <= hexvalue <= 9:
        return chr(hexvalue + ord("0"))
    else:
        return chr(hexvalue - 10 + ord("A"))

def main():
    decimalvalue = eval(input("Enter any value: "))

    print("The hex number for decimal",decimalvalue, "is", decimalToHex(decimalvalue))

main()