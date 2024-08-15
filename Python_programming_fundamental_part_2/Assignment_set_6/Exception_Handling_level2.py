# A 10-substring of a number is a substring of its digits that sum up to 10.

# For example, the 10-substrings of the number 3523014 are:
# 3523014, 3523014, 3523014, 3523014

# Write a python function, find_ten_substring(num_str) which accepts a string and returns the list of 10-substrings of that string.

# Handle the possible errors in the code written inside the function.


# Sample Input
# '3523014'

# Expected Output
# ['5230', '23014', '523', '352']

#lex_auth_01269442545042227276

def find_ten_substring(num_str):
    try:
        if not isinstance(num_str, str):
            raise ValueError("Input must be a string.")
        if not num_str.isdigit():
            raise ValueError("Input string must contain only digits.")
        
        result = []
        length = len(num_str)
        
        for i in range(length):
            current_sum = 0
            for j in range(i, length):
                current_sum += int(num_str[j])
                if current_sum == 10:
                    result.append(num_str[i:j+1])
                elif current_sum > 10:
                    break  # No need to continue if the sum exceeds 10
        
        return result
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        
        
num_str="2825302"
print("The number is:",num_str)
result_list=find_ten_substring(num_str)
print(result_list)