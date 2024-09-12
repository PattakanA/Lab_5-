height = int(input("Height: "))
if height < 1:
    print("Error")
for i in range(1, height + 1):
    print("#" * (height - i), "*" * (2 * i - 1),"#" * (height - i),sep="")