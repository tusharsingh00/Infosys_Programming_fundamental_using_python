# Given a string containing uppercase characters (A-Z), compress the string using Run Length encoding. Repetition of character has to be replaced by storing the length of that run.

# Write a python function which performs the run length encoding for a given String and returns the run length encoded String.

# Provide different String values and test your program


"""
--------------------------------------------------------------------------------------------------------------
        sample Input                                                          Expected Output
---------------------------------------------------------------------------------------------------------------
   AAAABBBBCCCCCCCC                            ||                              4A4B8C
   AABCCA                                      ||                              2A1B2C1A                
 ---------------------------------------------------------------------------------------------------------------
 
  """
  
  
# def encode(message):
#     for i in len(message):
        
#       pass

# encoded_message=encode("ABBBBCCCCCCCCAB")
# print(encoded_message)



def encode(s):
    from itertools import groupby
    return ''.join(f"{len(list(g))}{k}" for k, g in groupby(s))
encoded_message=encode("ABBBBCCCCCCCCAB")
print(encoded_message)