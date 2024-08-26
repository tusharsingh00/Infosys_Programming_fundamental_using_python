# Given two numbers, write a python function which returns true if first number is a seed of second number. Otherwise it returns false.

# A number X is said to be a seed of number Y, if multiplying X by its each digit equates to Y

# For example, 123 is a seed of 738 as 123*1*2*3 = 738.

# Sample Input
# 123,738
# 45,1000

# Expected Output
# True
# False


#lex_auth_0127135857243832321154

def seed_no(number,ref_no):
    num = 1
    for i in str(number):
        num *= int(i)
    num *= number  
    return (num == ref_no) 
        
    
number=123
ref_no=738
print(seed_no(number,ref_no))

