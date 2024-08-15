# Write a python function find_smallest_number() which accepts a number n and returns the smallest number having n divisors.
# Handle the possible errors in the code written inside the function.

# Sample Input
# 16

# Expected Output
# 120




#lex_auth_01269442760027340879

def nof(n):
    x=[]
    for i in range(1,n+1):
        if n%i==0:
            x.append(i)
    return x   
   
def find_smallest_number(num):
    n = 1
    while True:
        if len(nof(n)) == num:
            return n
        n += 1

num=16

print("The number of divisors :",num)
result=find_smallest_number(num)
print("The smallest number having",num," divisors:",result)