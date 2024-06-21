import sys


def menu():
    try:

        a = 'y'
        while a.lower() == 'y':
            print("--------------MENU------------")
            print("1.For calculator. \n2.For BMI. \n3.For Area. \n4.EXIT")
            choice = int(input("Enter your choice(1-4) : "))
            if choice == 1:
                calc()
            elif choice == 2:
                bmi()
            elif choice == 3:
                area()
            elif choice == 4:
                break
            else:
                print("Wrong input  ")
            input("Press ENTER KEY to continue......")
        else:
            sys.exit()
    except Exception as e:
        print("Error : ", e)

def calc():
    try:

        t = 'y'
        while t.lower() == 'y':
            print("------MENU---------")
            print("1.For Addition. \n2.For Subtraction \n3.For Multiplication \n4.For Division")
            ch = int(input("Enter your choice(1-4) : "))
            if ch == 1:
                n = int(input("Enter first number : "))
                n1 = int(input("Enter second number : "))
                print("Addition of the number is : ",n+n1)
            elif ch == 2:
                print("Do you want to ordinary subtract or you want to subtract by upper and lower number \nIf you want to ordinary subtract type 1 if you dont want that type 2")
                c = int(input("Enter your Choice(1-2) : "))
                if c == 1:
                    n = int(input("Enter first number : "))
                    n1 = int(input("Enter second number : "))
                    print("Subtraction of the number is : ",n - n1)
                elif c == 2:
                    n = int(input("Enter first number : "))
                    n1 = int(input("Enter second number : "))
                    high = n
                    low = n1
                    if n < n1:
                        high = n1
                        low = n
                    elif n > n1:
                        high = n
                        low = n1
                    else:
                        pass
                    print("Subtraction of the number is : ", high - low)
                else:
                    print("Wrong input")
            elif ch == 3:
                n = int(input("Enter first number : "))
                n1 = int(input("Enter second number : "))
                print("Multiplication of the number is : ", n * n1)
            elif ch == 4:
                print("Do you want to ordinary division or you want to divide by upper and lower lower number \nIf you want to ordinary division type 1 if you dont want that type 2")
                cs = int(input("Enter your Choice(1-2) : "))
                if cs == 1:
                    n = int(input("Enter first number : "))
                    n1 = int(input("Enter second number : "))
                    print("Division of the number is : ", n / n1)
                elif cs == 2:
                    n = int(input("Enter first number : "))
                    n1 = int(input("Enter second number : "))
                    high = n
                    low = n1
                    if n < n1:
                        high = n1
                        low = n
                    elif n > n1:
                        high = n
                        low = n1
                    else:
                        print("Invalid input")
                    print("Division of the number is : ", high / low)
            else:
                print("Wrong input")
            t = input("Do you want to continue(y/n) : ")
        else:
            print("Calculator close")
    except Exception as e:
        print("Error", e)

def bmi():
    try:
        h = float(input("Enter your Height : "))
        w = float(input("Enter your Weight : "))
        print("Your BMI is : ", h / w)
    except Exception as e:
        print("Error", e)

def area():
    try:
        print("1.For Area of rectangle. \n2.For Area of cirecle")
        s = int(input("Enter your choice(1-2) : "))
        if s == 1:
            l = float(input("Enter lenght of rectangle : "))
            b = float(input("Enter breadth of the rectangle : "))
            print("Area of rectangle is : ", l*b)
        elif s == 2:
            r = float(input("Enter radius of circle : "))
            print("Area of circle is : ", 3.14 * r * r)
        else:
            print("Wrong input")
    except Exception as e:
        print("Error", e)
menu()

