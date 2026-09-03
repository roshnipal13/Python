def checkEvenOdd(n):
    n = int(input("enter your number:"))
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(checkEvenOdd(7))