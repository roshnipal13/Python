a = input("enter:")
b = input("enter:")
num1 = int(a, 2)
num2 = int(b, 2)
sub = num1 - num2
if sub < 0:
    binary_sub = "-" + bin(abs(sub))[2:]
else:
    binary_sub = bin(sub)[2:]
print("decimal result", sub)
print("binary result", binary_sub)

     

     
