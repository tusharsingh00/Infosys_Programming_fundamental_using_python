# Write a python function which accepts a sentence and finds the number of letters and digits in the sentence.

# It should return a list in which the first value should be letter count and second value should be digit count. Ignore the spaces or any other special character in the sentence.

# Sample Input
# Infosys 123
# ABCEFG

# Expected Output
# [7,3]
# [6,0]



#lex_auth_0127135838317445121147


def count_digits_letters(sentence):
    letters = sum(c.isalpha() for c in sentence)
    digits = sum(c.isdigit() for c in sentence)
    return [letters, digits]  
    # return result_list

sentence="Infosys Mysore 570027"
print(count_digits_letters(sentence))