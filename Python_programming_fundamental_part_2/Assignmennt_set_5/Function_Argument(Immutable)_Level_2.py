
# Write a python function, check_double(number) which accepts a whole number and returns True if it satisfies the given conditions.

# The number and its double should have exactly the same number of digits.

# Both the numbers should have the same digits ,but in different order.

# Otherwise it should return False.

# Example: If the number is 125874 and its double, 251748, contain exactly the same digits, but in a different order.

#lex_auth_01269441810970214471


def check_double(number):
    double = number*2
    a=sorted(str(number))
    b=sorted(str(double))
    return a == b
    

print(check_double(125874))



#lex_auth_01269441810970214471

def check_double(number):
    double = number*2
    a=str(number)
    b=str(double)
    
    if len(a)!=len(b):  return False
       
    s=set(str(number))
 
    for i in s:
        if a.count(i)!=b.count(i): return False
           
    return True     
    

print(check_double(125874))