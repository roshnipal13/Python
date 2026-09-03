n = 1534
num = n 
nod = len(str(n))
total = 0
while num > 0:
    id = num % 10
    total = total + (id ** nod)
    num = num//10
print( total==n)
