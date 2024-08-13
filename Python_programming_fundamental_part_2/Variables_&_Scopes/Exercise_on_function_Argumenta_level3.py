# Write a Python function to find all the Strong numbers in a given list of numbers.
# Write another function to find and return the factorial of a number. Use it to solve the problem.

# Example:
# A number is considered to be a Strong number if sum of the factorial of its digits is equal to the number itself. 
# 145 is a Strong number as 1! + 4! + 5! = 145. 



#lex_auth_01269437118923571233

def factorial(number):
    if number == 0 or number == 1:
        return 1
    
    result = 1
    for i in range(2, number + 1):
        result *= i
    return result

def is_strong_number(num):
    return num == sum(factorial(int(digit)) for digit in str(num))

def find_strong_numbers(num_list):
    strong_numbers = [num for num in num_list if is_strong_number(num)]
    return strong_numbers

# Example usage
num_list = [145, 375, 100, 2, 10]
strong_num_list = find_strong_numbers(num_list)
print(strong_num_list)  

 
     
     