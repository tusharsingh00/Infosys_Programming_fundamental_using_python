""" Write a Python function which accepts a string and returns a string made of the first 2 and the last 2 characters of the given string.

If the string length is less than 2, return -1.

Note: If the string length is equal to 2, consider the 2 characters to be the first as well as the last two characters.

Sample Input
w3resource
w3
A

Expected Output
w3ce
w3w3
-1
""" 









#lex_auth_0127135945621340161163

def string_both_ends(input_string):
    if len(input_string) <= 1:
        return -1
    return(input_string[0:2]+input_string[len(input_string)-2:])
    

input_string="w3w"
print(string_both_ends(input_string))