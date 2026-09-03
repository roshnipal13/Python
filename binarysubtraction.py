a = input("enter your first binary number:")
b = input("enter your second binary number:")
sub_binary = int(a, 2) - int(b, 2)
sub_binary = bin(sub_binary)[2:]
print(sub_binary)
