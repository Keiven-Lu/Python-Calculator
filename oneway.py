#function for Addition
def add(fnum, snum):
    return fnum + snum
#function for Subtraction
def sub(fnum2, snum2):
    return fnum2 - snum2
#function for Multiplication
def mul(fnum3, snum3):
    return fnum3 * snum3
#function for Division
def div(fnum4, snum4):
    if fnum4 == 0:
        print("Can't divid by zero")
    elif snum4 == 0:
        print("Can't divide by zero")
    else:
        return fnum4 / snum4


#this is the main function
def main():
    while True:
        print("python calculator")
        print("choose an operation")
        print("1.Addition\n2.Subtraction\n3.Mutiplication\n4.Division")
        num = int(input("please enter a number(1/2/3/4)\n"))
        while num > 4:
            print("choose a number from 1-4")
            num = int(input("please try again"))
        if num == 1:
            fnum = float(input("Enter the first value: "))
            snum = float((input("Enter the second value: ")))
            result = add(fnum, snum)
            print(f"{fnum} + {snum} = {result}")
        elif num == 2:
            fnum2 = float(input("Enter the first value: "))
            snum2 = float((input("Enter the second value: ")))
            result2 = sub(fnum2, snum2)
            print(f"{fnum2} - {snum2} = {result2}")
        elif num == 3:
            fnum3 = float(input("Enter the first value: "))
            snum3 = float((input("Enter the second value: ")))
            result3 = mul(fnum3, snum3)
            print(f"{fnum3} * {snum3} = {result3}")
        elif num == 4:
            fnum4 = float(input("Enter the first value: "))
            snum4 = float((input("Enter the second value: ")))
            result4 = div(fnum4, snum4)
            print(f"{fnum4} / {snum4} = {result4}")
        else:
            print("Enter a number from 1-4")
        again = str(input("Let's do anther calculation (yes/no)\n"))
        if again == "yes":
            next = 0
            while next > 4:
                print("Invald number")
                next = int(input("please enter a number(1/2/3/4)\n"))
        else:
            print("bye")
            break
            
            
main()
