# Write a python function, find_correct() which accepts a dictionary and returns a list as per the rules mentioned below.
# The input dictionary will contain correct spelling of a word as key and the spelling provided by a contestant as the value.

# The function should identify the degree of correctness as mentioned below:
# CORRECT, if it is an exact match
# ALMOST CORRECT, if no more than 2 letters are wrong
# WRONG, if more than 2 letters are wrong or if length (correct spelling versus spelling given by contestant) mismatches.

# and return a list containing the number of CORRECT answers, number of ALMOST CORRECT answers and number of WRONG answers. 
# Assume that the words contain only uppercase letters and the maximum word length is 10.


def find_correct(word_dict):
    #start writing your code here
    ans=[0,0,0]
    for key,data in word_dict.items():
        if key == data:
            ans[0] += 1
        elif len(key) == len(data):
            count=0
            for i in range(len(key)):
                if key[i] != data[i]:
                    count += 1
            if count <= 2:
                ans[1] += 1
            else:
                ans[2] += 1
        else:
            ans[2] += 1
    return ans
    

word_dict={"THEIR": "THEIR","BUSINESS":"BISINESS","WINDOWS":"WINDMILL","WERE":"WEAR","SAMPLE":"SAMPLE"}
print(find_correct(word_dict))