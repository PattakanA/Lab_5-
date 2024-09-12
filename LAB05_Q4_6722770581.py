n = int(input("Enter an integer number (n>0): "))
print("(1) Factorial of n (n!)")
print("(2) Summation of n integers")
o = int(input("Select operation:"))
if n>0 and (o != 1 or o != 2):
    if o==1:
        f = 1
        for i in range(1, n + 1):
            f*= i
        print("Factorial of n (n!) = ",f)

    if o==2:   
        sum = 0
        for i in range(1, n + 1):
            sum += i
        print("Summation of n integers =",sum)
        
else:
    print("N/A Operation!")