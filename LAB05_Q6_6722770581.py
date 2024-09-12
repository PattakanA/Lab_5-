for i in range(5):
    n = int(input("enter a number between 1 and 20: "))
    if n<1 or n>20:
     print("number is invalid")
    else:
        if n%2 == 0:
              print(n," is an even number")
        else:
              print(n," is an odd number")
    
