# Write a python function, encrypt_sentence() which accepts a message and encrypts it based on rules given below and returns the encrypted message.
# Words at odd position -> Reverse It
# Words at even position -> Rearrange the characters so that all consonants appear before the vowels and their order should not change

# Note: 

# Assume that the sentence would begin with a word and there will be only a single space between the words.

# Perform case sensitive string operations wherever necessary.

""" 

# Sample Input                                               # Expected Output

 the sun rises in the east                                   eht snu sesir ni eht stea

"""


def encrypt_sentence(sentence):
    vowels = "aeiouAEIOU"
    
    def rearrange_word(word):
       
        consonants = [char for char in word if char not in vowels]
        vowels_in_word = [char for char in word if char in vowels]
        
        return ''.join(consonants + vowels_in_word)
    

    words = sentence.split()
    encrypted_words = []
    
    for index, word in enumerate(words):
        
        if (index + 1) % 2 != 0: 
            encrypted_words.append(word[::-1])
        else:
            encrypted_words.append(rearrange_word(word))
    

    return ' '.join(encrypted_words)


sentence = "The quick brown fox jumps over the lazy dog"
encrypted_message = encrypt_sentence(sentence)
print(encrypted_message)
