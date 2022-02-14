import sys


def menu():

    a = 'y'
    while a.lower() == 'y':
        print("""
            1. TO calculate the area of rectangle.
            2. To calculate the area of circle.
            3. Students records.
            4. To convert feet into inches.
            5. To convert fahrenheit into celsius.
            6. To find the volume of the cylinder.
            7. To give the bonus to employee.
            8. To find two larger number.
            9. To find three larger number.
            10. To check for eligible for vote or not.
            11. To check the number is even or odd.
            12. To check the user are teenager or not.
            13. To give commission to employee,
            14. To check leap year or not.
            15. To check absolute value of number.
            16. To find out positive or negative number.
            17. To check water physical state.
            18. To check the type of triangle.
            19. To find about the character.
            20. EXIT""")

        try:
            n = int(input("Enter the choice given above(1-20) : "))

            if n == 1:
                rectangle()
            elif n == 2:
                circle()
            elif n == 3:
                record()
            elif n == 4:
                distance()
            elif n == 5:
                temp()
            elif n == 6:
                volume()
            elif n == 7:
                bonus()
            elif n == 8:
                large()
            elif n == 9:
                large2()
            elif n == 10:
                vote()
            elif n == 11:
                check()
            elif n == 12:
                teen()
            elif n == 13:
                sale()
            elif n == 14:
                leap()
            elif n == 15:
                val()
            elif n == 16:
                num()
            elif n == 17:
                state()
            elif n == 18:
                triangle()
            elif n == 19:
                search()
            elif n == 20:
                break
            else:
                print("Invalid input")
            input("Press ENTER KEY to continue...")

        except Exception as e:
            print("Error : ", e)

    else:
        sys.exit()


def rectangle():
    # 1). Area of rectangle

    l = int(input("Enter length : "))
    b = int(input("Enter breadth : "))
    print("Area of rectangle : ", l * b)

def circle():

    # 2). Area of circle.

    r = float(input("Enter radius of circle"))
    print("Area of circle :", 3.14*r*r)

def record():

    # 3). To enter name,marks of 5 subject and calculate total and percentage.

    name = input("Enter Name")
    phy = float(input("Enter marks of physics : "))
    chem = float(input("Enter marks of chemistry : "))
    math = float(input("Enter marks of mathematics : "))
    cs = float(input("Enter marks of computer science : "))
    eng = float(input("Enter marks of English : "))
    total = phy+chem+math+cs+eng
    per = total/5
    print(name, "has scored total", total, "and percentage", per, "%")

def distance():

    # 4). Distance in feet and convert into inches.

    f = float(input("Enter distance in feet : "))
    print("Feet in inches", f*12)

def temp():

    # 5). Temperature in fahrenheit convert into celsius

    fh = float(input("Enter temperature in fahrenheit : "))
    print("Fahrenheit to celsius : ", (fh-32)*5/9)

def volume():
    # 6). Volume of cylinder

    R = float(input("Enter radius : "))
    H = float(input("Enter height : "))
    print("Volume of cylinder : ", 3.14*R*R*H)

def bonus():

    # 7). Bonus.

    Bonus = 0
    sale = int(input("Enter monthly sale : "))
    if sale >= 50000:
        Bonus = sale * 10/100
    print("Bonus = ", str(Bonus))

def large():

    # 8). 2 larger number

    n1 = int(input("Enter first number : "))
    n2 = int(input("Enter second number : "))
    large = n1
    if large < n2:
        large = n2
    print("Largest number is : ", large)

def large2():

    #9). 3 larger number

    n1 = int(input("Enter first number : "))
    n2 = int(input("Enter second number : "))
    n3 = int(input("Enter third number : "))
    large = n1
    if large < n2:
        large = n2
    if large < n3:
        large = n3
    print("Largest number is : ", large)

def vote():

    #10). eligible for vote or not

    age = int(input("Enter your age : "))
    if age >= 18:
        print("Congratulation! You are eligible for vote.")
    else:
        print("Sorry! You are not eligible for vote")

def check():

    #11). Check even or odd

    num = int(input("Enter number : "))
    if num % 2 == 0:
        print(num, "is even number.")
    else:
        print(num, "is odd number.")

def teen():

    #12). to check teenager or not

    age = int(input("Enter your age : "))
    if 12 < age < 18:
        print("He/She is teenager.")
    else:
        print("He/She is not a teenager.")

def sale():

    #13). enter monthly sale and give him commission in followings

    monthly_sale = float(input("Enter monthly sale : "))
    if monthly_sale > 50000:
        print("Commission will be :", monthly_sale*10/100)
    else:
        print("Commission will be :", monthly_sale*5/100)

def leap():

    #14). Check leap year or not

    year = int(input("Enter year : "))
    if year % 4 == 0:
        print("It is a leap year.")
    else:
        print("It is not a leap year.")

def val():

    #15). Absolute value of a number

    num = float(input("Enter number : "))
    print("The absolute number is : ", abs(num))

def num():

    #16). Find out positive or negative number

    num = int(input("Enter number : "))
    if num > 0:
        print("It is positive number.")
    elif num == 0:
        print("It is zero.")
    else:
        print("It is negative number.")

def state():

    #17). temperature of water and its physical state

    temp = int(input("Enter temperature of water : "))
    if temp > 100:
        print("Gasses state.")
    elif temp < 0:
        print("Solid state.")
    else:
        print("Liquid state.")

def triangle():

    #18). 3 side of triangle and type of triangle

    s1 = int(input("Enter side 1 : "))
    s2 = int(input("Enter side 2 : "))
    s3 = int(input("Enter side 3 : "))
    if s1 == s2 == s3:
        print("Equilateral triangle.")
    elif s1 != s2 != s3:
        print("Scalene triangle.")
    else:
        print("Isoceles triangle.")

def search():

    #19). To find character is uppercase,lowercase,digit or symbol

    ch = input("Enter a character : ")
    if ch.isupper():
        print("Uppercase.")
    elif ch.islower():
        print("Lowercase.")
    elif ch.isdigit():
        print("Digit.")
    else:
        print("Symbol.")
menu()
