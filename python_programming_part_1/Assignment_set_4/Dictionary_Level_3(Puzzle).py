# Problem Statement
# Write a python program that accepts a text and displays a string which contains the word with the largest frequency in the text and the frequency itself separated by a space.

# Rules:

# The word should have the largest frequency.

# In case multiple words have the same frequency, then choose the word that has the maximum length.

# Assumptions:

# The text has no special characters other than space.

# The text would begin with a word and there will be only a single space between the words.


"""
--------------------------------------------------------------------------------------------------------------
        sample Input                                                          Expected Output
---------------------------------------------------------------------------------------------------------------

"Work like you do not need money love like you                  ||
have never been hurt and dance like no one is watching"         ||                like 3
   
                                                                                                       
"Courage is not the absence of fear but rather the              ||
judgement that something else is more important than fear"      ||                 fear 2

---------------------------------------------------------------------------------------------------------------
 
  """
  
  
#   #lex_auth_0127382283825971201450

# def max_frequency_word_counter(data):
#     word=[]
#     words =""
#     frequency=0
#     data = data.split()
    
#     for i in data:
#         if i not in word:
#             word.append(i)
    
#     for i in range(0,len(word)):
#         if data.count(word[i]) > frequency:
#             frequency = data.count(word[i]) 
#             words = word[i]

#     if frequency == 1:
#         for i in data:
#             if len(i) > frequency:
#                 frequency = len(i)
#                 word = i
        
            
#     print(words,frequency)




#? SOLUTION 1


def max_frequency_word_counter(data):
    word=""
    frequency=0

    words = data.lower().split()
    word_counts = {word: words.count(word) for word in set(words)}
    word, frequency = max(word_counts.items(), key=lambda item: (item[1], len(item[0])))
    print(word, frequency)

   
data="Work like you do not need money, love like you have never been hurt, and dance like no one is watching"
max_frequency_word_counter(data)



#? SOLUTION 2

#lex_auth_0127382283825971201450

def max_frequency_word_counter(data):
    word=""
    frequency=0

    #start writing your code here
    #Populate the variables: word and frequency
    dict={}
    data1=data.lower()
    list=data1.split()
    my_set=set(list)
    list2=[]
    
    for i in my_set: dict[i]=list.count(i)
    
    max=0
    
    for key,value in dict.items():
        if max<dict[key]:
            max=dict[key]
    #list3=[]
    list2=[]
    frequency=max
    for key,value in dict.items():
        if max==dict[key]:
            list2.append(key)
    
    word=list2[0]
    for i in range(1,len(list2)):
        if len(word)<len(list2[i]):
            word=list2[i]
    
    print(word,frequency)


    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work
    #print(word,frequency)


#Provide different values for data and test your program.
data="Work like you do not need money, love like you have never been hurt, and dance like no one is watching"
max_frequency_word_counter(data)

