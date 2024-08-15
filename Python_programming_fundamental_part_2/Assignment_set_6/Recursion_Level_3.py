# Write a python function find_duplicates(), which accepts a list of numbers and returns another list containing all the duplicate values in the input list and the order should be same as in the input list. If there are no duplicate values, it should return an empty list.


# Sample Input
# [12,54,68,759,24,15,12,68,987,758,25,69]

# Expected Output
# [12, 68]



 #lex_auth_01269443477535129681

def find_duplicates(list_of_numbers):
    duplicate = []
    for i in list_of_numbers:
        if list_of_numbers.count(i)> 1 and i not in duplicate:
            duplicate.append(i)
    return duplicate
    #start writing your code here

list_of_numbers=[1,2,2,3,3,3,4,4,4,4,5]
list_of_duplicates=find_duplicates(list_of_numbers)
print(list_of_duplicates)

