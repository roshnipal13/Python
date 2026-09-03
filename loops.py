#wap to find a sum of all the even numbers up to 50.
#for i in range(0, 51):
    #if i % 2 == 0:
       #sum += i
       # print(i)
#wap to write first 20 numbers and their squared numbers
#for i in range(1, 21):
    #print(i * i)

#wap to find sum of first 10 odd numbers using while loop 
#n = 0
#sum = 0
#while n <= 20:
    #if n % 2 != 0:
        #sum += n
    #n += 1
#print(sum)

#wap to check ## a number is divisible by 8 and 12 up to 100 numbers
#for i in range(1, 101):
    #if i % 8 == 0 and i % 12 == 0:
        #print(i)
#wap to create a billing system at supermaarket
while True:
    name = input()
    total = 0
    while True:
        print("enter the amount and quantity")
        amount = float(input("enter amount:"))
        quantity = float(input("enter quantity:"))
        total += amount * quantity
        repeat = input("do you want to add item? (yes/ no)")
        if repeat =="no" or repeat == "No":
            break
    print("-"*40)
    print("Name:",name)
    print("amount",total)
    print("-"*40)
    print("**shopping**")
    repeat1 = input()
    if repeat1 == "no" or repeat == "No":
        break



