#Enter a number and check whether it is 10 or not

a=int(input("Enter A : "))

if a==10:
    print("Equal to 10")
else:
    print("Not Equal to 10")

# Find largest of two numbers

a=int(input("Enter A: "))
b=int(input("Enter B: "))

if a>b:
    g=a
else:
    g=b

print("Greater = ",g)

#Find largest of two numbers using single statement

a=int(input("Enter A: "))
b=int(input("Enter B: "))

c= a if a>b else b

print("Greater = ",c)