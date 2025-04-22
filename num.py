num = int (input("Enter a number: "))
t = num
a = 0
while (t > 0):
    t = t // 10
    a = a + 1

if a == 4: 
    a = int (a/2)
    b = 0
    while num > 0:
        c= num % 10
        if b == a:
            Midone = c
        elif b ==(a - 1):
            Midtwo = c
        num = int (num / 10)
        b = b + 1
        prod = Midone * Midtwo
    print ("The product of the middle two digits is: ", prod)
else:
    print ("The number is not a 4 digit number")