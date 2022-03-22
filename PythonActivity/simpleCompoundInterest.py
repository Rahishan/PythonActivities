# Python program to find simple interest 

p = float(input("Enter the principle amount : "))
r = float(input("Enter the rate of interest : "))
t = float(input("Enter the time in the years: "))

# calculating simple interest
si = (p*r*t)/100

# printing the values
print("Principle amount: ", p)
print("Interest rate   : ", r)
print("Time in years   : ", t)
print("Simple Interest : ", si)

# Python program to find compound interest 

p = float(input("Enter the principle amount : "))
r = float(input("Enter the rate of interest : "))
t = float(input("Enter the time in the years: "))

# calculating compound interest
ci =  p * (pow((1 + r / 100), t)) 

# printing the values
print("Principle amount  : ", p)
print("Interest rate     : ", r)
print("Time in years     : ", t)
print("compound Interest : ", ci)