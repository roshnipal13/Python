"""n = int(input("enter your number"))
if n >= 0:
    print("positive")
else:
    print("negative")"""
#wapto check whether a number is odd or even
"""num = int(input("enter your number"))
if num % 2 == 0:
    print("even")
else:
    print("odd")"""
#wap to create area calculater
"""print("*******AREA******")
#print(ress 1 to get the area of squr)
      ###press 4 to get area of triengle"""
"""n = int(input("enter your number 1-4: "))
if n == 1:
    side = float(input("enter the length of one side: "))
    area = side**2
    print("the area of square is:", area)
elif n == 2:
    length = float(input("enter the values of the length:"))
    width =  float(input("enter your width"))
    area = length * width
    print("the are of rectangular is:", area)
elif n == 3:
    radius = float(input("enter the radius of the circle:"))
    area = 3.14*radius**2
    print("area of circle is:", area)
elif n == 4:
    base = int(input("enter your base:"))
    height = int(input("enter your height:"))
    area = (1/2)* base*height
    print("area of tringle:",area)"""
# wap to check wheter the passed letter is a vowel or not
"""letter = input("enter your letter here :")
if letter in "aeiou":
    print("vowel")
else:
    print("not")"""
#wap to check if a number is a single digit number, 2 digit number and so on... up to 5 digits:
n = int(input("enter a number here upto 5 digits: "))
if n >= 0 and n < 9:
    print("single digit:")
elif n >=  10 and n < 99:
    print("double digits")
elif n >= 100 and n < 999:
    print("triple digit")
elif n >= 1000 and n < 9999:
    print("four digit")
elif n >= 10000 and n < 9999:
    print("five digit")
else:
    print("invaild")



