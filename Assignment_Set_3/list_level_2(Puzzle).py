# Write a python function, create_largest_number(), which accepts a list of numbers and returns the largest number possible by concatenating the list of numbers. 
# Note: Assume that all the numbers are two digit numbers.

def create_largest_number(number_list):
    
    number_list.sort()
    number_list.reverse()
    number_list = ''.join(str(num) for num in number_list)
    return number_list

number_list=[23,45,67]
largest_number=create_largest_number(number_list)
print(largest_number)