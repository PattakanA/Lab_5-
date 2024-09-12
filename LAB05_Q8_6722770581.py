print("Menu:")
print("A - Americano (50)")
a = "A - Americano (50)"
print("E - Espresso (40)")
e = "E - Espresso (40)"
print("G - Green tea (60)")
g = "G - Green tea (60)"
txt = input("Input: ")
n=0
tot = 0
for i in txt:
    if i == "A" or i =="E" or i == "G":
         n += 1
   
    print("%d." % n ,end="")
    if i == "A":
        print(a)
        tot += 50
    elif i == "E":
        print(e)
        tot += 40
    elif i == "G":
        print(g)
        tot += 60

v = tot * 0.07
gtot = tot + v
print("Quantity: ",n)
print("Total:  %.2f baht" %tot)
print("VAT :  %.2f baht" %v)
print("Grand Total:  %.2f baht"%gtot)
