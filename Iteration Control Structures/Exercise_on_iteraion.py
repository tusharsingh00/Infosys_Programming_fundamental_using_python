
#TODO Write a Python program to find the sum of digits of a given number. E.g. Sum of number 123 will be 6

#! Note: Initialize the number with various values and test your program.

#lex_auth_012693749623193600122

# def find_sum_of_digits(number):
#     sum_of_digits=0
#     #Write your logic here
#     return sum_of_digits

# #Provide different values for number and test your program
# sum_of_digits=find_sum_of_digits(123)
# print("Sum of digits:",sum_of_digits)

#?    SOLUTION

# ?   #################################################

# def find_sum_of_digit(n):
#     return sum((int(i)) for i in str(n))

# sum_of_digits=find_sum_of_digit(333)
# print("Sum of digits:",sum_of_digits)

#?   #################################################


# def find_sum_of_digit(number):
#     sum_of_digit = 0
#     strs = str(number)
#     for i in (strs):
#          sum_of_digit += int(i) 
#     return sum_of_digit
        
        
# sum_of_digits=find_sum_of_digit(333)
# print("Sum of digits:",sum_of_digits)

# #?   #################################################


# def find_sum_of_digits(numbers):
#     sum_of_digits =  0
def getSum(n):
    sum = 0
    while n != 0:
        sum += n % 10
        n //= 10
    return sum

n = 12345
print(getSum(n))  # Output: 15


##?   #################################################


def getSum(n):
    return sum(map(int, str(n)))

n = 12345
print(getSum(n))  # Output: 15
