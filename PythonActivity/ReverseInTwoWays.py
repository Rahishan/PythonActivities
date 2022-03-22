 # WAY 1Famous approach for reversing the number: Take input 
 # from the user and typecast into an integer, then iterate in the loop till num is not become zero, inside the loop:

#Find out the remainder.
#Using this: rev_num = rev_num * 10 + remainder.
#Update that number by diving by 10.
#After coming out of the loop printing the reverse number.

if __name__ == "__main__" :

    # take string input from user
    num = int(input('Enter a number: '))

    rev_num = 0

    # iterate the loop till num is not equal to zero
    while(num) :
        rem = num % 10
        rev_num = rev_num* 10 + rem
        num //= 10
    
    print('Reverse number is: ', rev_num)

# WAY 2 Make a user-defined function for reversing the Number: 
# Take input from the user and typecast into integer, thenreverseNum() function call.

#Inside the function:

#Iterate in the loop till num does not become zero:
#Find out the remainder.
#Using this: rev_num = rev_num * 10 + remainder.
#Update that number by diving by 10.
#After coming out of the loop returning the reverse number to the main.
# define a function for finding 
# reverse of the number
def reverseNum(num) :
    
    rev_num = 0

    # iterate the loop till num is not equal to zero
    while(num) :
        rem = num % 10
        rev_num = rev_num* 10 + rem
        num //= 10

    return rev_num


# Main() method
if __name__ == "__main__" :

    # take string input from user
    num = int(input('Enter a number: '))
    
    print('Reverse number is: ', reverseNum(num))