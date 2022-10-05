global num
def numberconverter():
    num = 0
    print("")
    mainmenu()
    selection = int(input("Please chose an option "))

    if (selection == 3):
        print("you have exited the program")
        exit()

    while num <= 0 or num >= 1000:
        num = int(input("please input a number to convert from 0 to 1000!"))
        if num in range(0, 1000):
            print(num, "is in the range of 0-1000")
        else:
            print("the number is outside the given range,please try again")



    if (selection == 1):
        decimalToBinary(num)
        print('....')



    if (selection == 2):
        decimalToHex(num)
        if (num == 1):
            print("2"),
        if (num == 2):
            print("2"),
        if (num == 3):
            print("3"),
        if (num == 4):
            print("4"),
        if (num == 5):
            print("5"),
        if (num == 6):
            print("6"),
        if (num == 7):
            print("7"),
        if (num == 8):
            print("8"),
        if (num == 9):
            print("9"),
        if (num == 10):
            print("A"),
        if (num == 11):
            print("B"),
        if (num == 12):
            print("C"),
        if (num == 13):
            print("D"),
        if (num == 14):
            print("E"),
        if (num == 15):
            print("F"),
        if (num == 16):
            print("10(1+0)"),
        if (num == 17):
            print("11(1+1)"),

            print('....')

            if (selection < 1 or selection > 3):
             print("incorrect command, try again")
             mainmenu()


def mainmenu():
    print("1. convert decimal number to binary")
    print("2. convert a decimal number to hexadecimal")
    print("3. exit program")

def decimalToBinary(value):
    global num
    num = 0
    if value >= 1:
        decimalToBinary(value // 2)
    return print(value % 2)

def decimalToHex(value):
    if (value < 0):
        print(0)
    elif (value <= 1):
        print
        value,
    else:
        decimalToHex(value / 16)
    return (value % 16)


while True:
    print("welcome to the decimal converter program")
    numberconverter()

