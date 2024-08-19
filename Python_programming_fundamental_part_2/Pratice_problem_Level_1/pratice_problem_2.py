'''
Write a python function which accepts a string containing a pattern of brackets and returns true if the pattern of brackets is correct. Otherwise it returns false.

The string of brackets is correct if it satisfies the following conditions:
1. Number of opening and closing brackets are equal.
2. Pattern should not start with closing bracket and end with opening bracket.

Sample Input
)()((()())
()((())())

Expected Output
False
True
'''

#lex_auth_0127135773590405121141

#lex_auth_0127135773590405121141

def bracket_pattern(input_str):
    if input_str[0] in ")" or input_str[-1] in "(":
           return False
    
    # Stack to keep track of opening brackets
    c = 0
    for i in input_str:
       
        if i == "(":
            c += 1
        elif i == ")":
            c -= 1
        
    return(c==0)

    
input_str="(())("
print(bracket_pattern(input_str))




