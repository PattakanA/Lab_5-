inp = input("Input: ")
if len(inp) == 9:
  for i in inp:
    if i not in "X.O":
      print("Error")
      break
    else:
      print("-------")
      for j in range(0,9,3):
        print("|%s|%s|%s|"%(inp[j],inp[j+1],inp[j+2]))
        print("-------")
      break
else:
  print("Error")
      