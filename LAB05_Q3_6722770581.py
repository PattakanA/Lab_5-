sum = 0
print("Multiplication table:")
no=int(input("Please enter number between 1 to 25: "))
print("multiplication table of", no)
if no>=0 and no<=25:
    for i in range(1,13,1):
        print("%d * %d = %d" %(no,i,(no*i)))
else:
    print("You entered invalid number")
