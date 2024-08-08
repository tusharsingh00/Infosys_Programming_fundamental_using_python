# Problem Statement

#TODO Write a python function to check whether three given numbers can form the sides of a triangle. 

#* Hint : Three numbers can be the sides of a triangle if none of the numbers are greater than or equal to the sum of the other two numbers.

#######################################################################################################

# #lex_auth_012693802383794176153

# def form_triangle(num1,num2,num3):
#     #Do not change the messages provided below
#     success="Triangle can be formed"
#     failure="Triangle can't be formed"

#     #Write your logic here

#     #Use the following messages to return the result wherever necessary
#     return success
#     return failure

# #Provide different values for the variables, num1, num2, num3 and test your program
# num1=3
# num2=3
# num3=5
# form_triangle(num1, num2, num3)

###############################################################################################################


# SOLUTION

def form_triangle(num1,num2,num3):
    success = "Triangle can be Formed"
    failure = "Triangle can't formed"
    
    if  (num1 + num2 <= num3) or (num1 + num3 <= num2) or (num2 + num3 <= num1):
        print(success)
    else:
        print(failure)
    
    return "return",success if (num1 + num2 <= num3) or (num1 + num3 <= num2) or (num2 + num3 <= num1) else failure
        
# form_triangle(9,3,3)
print(form_triangle(9,18,9))