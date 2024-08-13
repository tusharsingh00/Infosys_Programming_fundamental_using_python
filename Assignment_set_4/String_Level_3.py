# Write python function, sms_encoding() which accepts a sentence and converts it into an abbreviated sentence to be sent as SMS and returns the abbreviated sentence. 

# Rules are as follows: 
# a. Spaces are to be retained as is 
# b. Each word should be encoded separately

# If a word has only vowels then retain the word as is

# If a word has a consonant (at least 1) then retain only those consonants

# Note: Assume that the sentence would begin with a word and there will be only a single space between the words.



# def sms_encoding(data):
#     vowel = "aeiouAEIOU" 
#     encode = []
#     for i in data:
#         if i in vowel: data = data.replace(i,"")

#     return data
    

# data="I love Python"
# print(sms_encoding(data))




def sms_encoding(data):
    vowels = "aeiouAEIOU"
    words = data.split()  
    encoded_words = []

    for word in words:
        if all(char in vowels for char in word):
            encoded_words.append(word)
        else:
            consonants = ''.join([char for char in word if char not in vowels])
            encoded_words.append(consonants)

    return ' '.join(encoded_words)

data="I love Python"
print(sms_encoding(data))