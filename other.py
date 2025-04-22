ur = int (input("Enter an upper range: "))
lr = int (input("Enter a lower range: "))
print ("The prime numbers between ", lr, " and ", ur, " are:")
for num in range (lr, ur + 1):
    if num > 1:
        for i in range (2, num):
            if (num % i) == 0:
                break
        else:
            print (num)