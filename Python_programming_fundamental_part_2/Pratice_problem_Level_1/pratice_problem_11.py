
# Write a python function which accepts a sentence and returns a list in which first value is the count of upper case letters and second value is the count of lower case letters in the sentence. Ignore spaces, numbers and other special characters if any.

# Sample Input
# Hello world!
# Welcome to Mysore

# Expected Output
# [1,9]
# [2,13]





#lex_auth_0127136021907046401165

def find_upper_and_lower(sentence):
    upper_count = 0
    lower_count = 0
    
    for char in sentence:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    
    return [upper_count, lower_count]

sentence="Come Here"
print(find_upper_and_lower(sentence))