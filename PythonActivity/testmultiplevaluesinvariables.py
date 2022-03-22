a = 10
b = 20
c = 30

# method 1
if a == 10 or b == 10 or c == 10:
  print("True")
else:
  print("False")  

# method 2
if 10 in (a, b, c):
  print("True")
else:
  print("False")  

# method 3
if 10 in {a, b, c}:
  print("True")
else:
  print("False")  