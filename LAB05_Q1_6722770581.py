even,odd = 0,0
for i in range(5):
  n = int(input("enter a number: "))
  if n%2 == 0:
    even += 1
  else:
    odd += 1
print("there were %d even numbers"%even)
print("there were %d odd numbers"%odd)