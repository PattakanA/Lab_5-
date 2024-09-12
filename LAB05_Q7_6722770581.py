l, s, h = 0, 0, 0
c = 0
for i in range(10):
  n = input('Feeling Like ("L"), Sad ("S"), and Heart("H")? ')
  if (n == "L" or n == "S" or n == "H"):
    if n == "L":
      l += 1
    elif n == "S":
      s += 1
    elif n == "H":
      h += 1
    c += 1
  else:
    print("Invalid input, accepts only (L/S/H).")

if c > 0:
  hp = (h / c) * 100
  lp = (l / c) * 100
  sp = (s / c) * 100
  print("Like: %d (%.2f%%)" % (l, lp))
  print("Sad: %d (%.2f%%)" % (s, sp))
  print("Heart: %d (%.2f%%)" % (h, hp))
else:
  print("Like: 0 (0.00%)")
  print("Sad: 0 (0.00%)")
  print("Heart: 0 (0.00%)")