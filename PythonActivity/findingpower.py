# python program to find the power of a  Integer number

a = 10
b = 3

# calculating power using exponential oprator (**)
result = a**b

print (a, " to the power of ", b, " is = ", result)

# python program to find the power of a  Float number

a = 10.23
b = 3.2

# calculating power using exponential oprator (**)
result = a**b

print (a, " to the power of ", b, " is = ", result)


# Python code to find power of a number using loop
num = int(input("Enter the number of which you have to find power: "))
pw = int(input("Enter the power: "))

kj = 1
for n in range(pw):
    kj = kj*num

print(kj)

#Given the base x and the power y and we have to find the x to the power y using recursion in Python.

#By using recursion – We will be multiplying a number (initially with value 1) by the number input by the user (of which we have to find the value of yth power) for y times. For multiplying it by y times, we need to call our function y times. Since we know the number of times function will execute, so we are using for recursion. 

#Python code to find the power of a number using recursion

# Python code to find the power of a number using recursion 

# defining the function to find the power
# function accpets base (x) and the power (y)
# and, return x to the power y
def pow(x, y):
    if y == 1:
        return x
    else:
        return pow(x, y-1) * x

# main code
if __name__ == '__main__':
    x = 2 #base
    y = 3  #power
    result = pow(x, y)
    print(x," to the power ", y, " is: ", result)

    x = 10 #base
    y = 3  #power
    result = pow(x, y)
    print(x," to the power ", y, " is: ", result)
    
    x = 12 #base
    y = 5  #power
    result = pow(x, y)
    print(x," to the power ", y, " is: ", result)

