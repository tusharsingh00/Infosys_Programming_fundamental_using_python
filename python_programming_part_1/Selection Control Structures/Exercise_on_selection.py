
#TODO Write a python program that displays a message as follows for a given number:

#* If it is a multiple of three, display "Zip"
#* If it is a multiple of five, display "Zap".
#* If it is a multiple of both three and five, display "Zoom".
#* If it does not satisfy any of the above given conditions, display "Invalid".


###################################################

# #lex_auth_01269363490743091290

# def display(num):
#     message=""
#     #write your logic here
#     return message

# #Provide different values for num and test your program
# message=display(9)
# print(message)

###################################################

#? SOLUTION

def display(num):
    message = ""
    if num%3==0 and num % 5==0:
        message = "Zoom"
    elif num %3 == 0:
        message = "Zip"
    elif num%5 == 0:
        message = "Zap"
    else:
        message = "invalid"
    return message

print(display(14)) 
