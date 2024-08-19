#lex_auth_0127135787454873601143
# Write a python function to create and return a new dictionary from the given dictionary(item:price).

# Given the following input, create a new dictionary with elements having price more than 200.

# prices = {'ACME': 45.23,'AAPL': 612.78, 'IBM': 205.55,'HPQ': 37.20,'FB': 10.75}


def create_new_dictionary(prices):
    new_dict ={}
    for key, value in  prices.items():
        if value > 200:
            new_dict = {key,value}
            print(key,value)
    
    return new_dict

prices = { 'ACME': 45.23,'AAPL': 612.78,'IBM': 205.55,'HPQ': 37.20,'FB': 10.75}
print(create_new_dictionary(prices))