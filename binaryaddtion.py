a = input("enter your binary number:")
b = input("enter your second binary number:")
sum_decimal = int(a, 2) + int(b, 2)
sum_binary = bin(sum_decimal)[2:]
print(sum_binary)