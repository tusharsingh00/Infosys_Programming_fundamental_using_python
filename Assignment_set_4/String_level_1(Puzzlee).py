

# Write a python program to display all the common characters between two strings. Return -1 if there are no matching characters.

# Note: Ignore blank spaces if there are any. Perform case sensitive string comparison wherever necessary.


"""
--------------------------------------------------------------------------------------------------------------
        sample Input                                                          Expected Output
---------------------------------------------------------------------------------------------------------------
                                                                         ________________
"I like Python"                                 ||                      |               |
"Java is a very popular language"               ||                      |    lieyon     |
                                                                        |_______________|
---------------------------------------------------------------------------------------------------------------
 
  """





def find_common_characters(msg1,msg2):

    msg=''
    for i in msg1:
        if i in msg2 and i not in msg:
            msg+=i
    if len(msg) == 0:
        msg =-1
    return msg

#Provide different values for msg1,msg2 and test your program
msg1="I like Python"
msg2="Java is a very popular language"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)





# def find_common_characters(msg1,msg2):
    
#     msg1=msg1.replace(' ',"")
#     for  n  in msg1:
#         if n  not in  msg2:
#             msg1 = msg1.replace(n,'')
#     if len(msg1) ==0:
#        msg1 = -1
#     return msg1   
        
        # print("n",n)
     #Remove pass and write your logic here

#Provide different values for msg1,msg2 and test your program
# msg1="I like Python"
# msg2="Java is a very popular language"

msg1="Moto"
msg2="Moto"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)



