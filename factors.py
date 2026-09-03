"""n = int(input("enter your number :"))
result = []
for i in range(1 , n+1):
    if n % i==0:
        result.append (i)

print(result)"""
n = 20
result = []
for i in range(1, n//2):
    if n % 10 == 0:
        result.append(i)
result.append(n)
print(result)

