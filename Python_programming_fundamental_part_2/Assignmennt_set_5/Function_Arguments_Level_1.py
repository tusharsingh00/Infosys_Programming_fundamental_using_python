# Write a python function, find_pairs_of_numbers() which accepts a list of positive integers with no repetitions and returns count of pairs of numbers in the list that adds up to n. The function should return 0, if no such pairs are found in the list.
 
 
""" 
Sample Input

[3, 4, 1, 8, 5, 9, 0, 6], 9
[1, 2, 7, 4, 5, 6, 0, 3], 6

Expected Output

4
3
"""


#lex_auth_01269438594930278448

def find_pairs_of_numbers(num_list,n):
    num_list.sort()
    
    ans =0
    for i in range(len(num_list)):
        for j in range(i+1,len(num_list)):
            if num_list[i]+num_list[j]>n:
                break
            elif num_list[i]+num_list[j]==n:
                ans +=1
    return ans    
    #Remove pass and write your logic here

num_list=[1, 2, 4, 5, 6]
n=6
print(find_pairs_of_numbers(num_list,n))


