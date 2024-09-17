def add(fnum, snum):
    fnum = float(input("Enter the first value: "))
    snum = float((input("Enter the second value: ")))
    result = fnum + snum
    return(f"{fnum} + {snum} = {result}")
def sub(fnum2, snum2):
    fnum2 = float(input("Enter the first value: "))
    snum2 = float(input("Enter the second value: "))
    result2 = fnum2 - snum2
    return(f"{fnum2} - {snum2} = {result2}")
def mul(fnum3, snum3):
    fnum3 = float(input("Enter the first value: "))
    snum3 = float(input("Enter the second value: "))
    result3 = fnum3 * snum3
    return(f"{fnum3} * {snum3} = {result3}")
def div(fnum4, snum4):
    fnum4 = float(input("Enter the first value: "))
    snum4 = float(input("Enter the second value: "))
    result4 = fnum4 / snum4
    return(f"{fnum4} / {snum4} = {result4}")



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
            result = add(0, 0)
            print(result)
        elif num == 2:
            result2 = sub(0, 0)
            print(result2)
        elif num == 3:
            result3 = mul(0, 0)
            print(result3)
        elif num == 4:
            result4 = div(0, 0)
            print(result4)
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
