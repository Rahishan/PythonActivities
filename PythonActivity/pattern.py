#pattern 1 

for row in range (0,5):
    for column in range (0, row+1):
        print ("*", end="")

    # ending row
    print('\r')

#Pattern 2 row operation
for row in range(0,5):

# column operation

    for column in range(0,row+1):
        print("1 ",end="")

    # ending line
    print('\r')

# Pattern 3
#row operation
for row in range (0, 5):
    n = 1
    # column operation
    for column in range (0, row+1):
        print(n, end=" ")
        n = n+1
    # ending line
    print('\r')

# Pattern 4
n = 1
#row operation
for row in range (0, 5):

    # column operation
    for column in range (0, row+1):
        print(n, end=" ")
        n = n+1
    # ending line
    print('\r')

# Pattern 5

#row operation
for row in range (0, 5):
    n = 65
    # column operation
    for column in range (0, row+1):
        c = chr(n)
        print(c, end=" ")
        n = n+1
    # ending line
    print('\r')