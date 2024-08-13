# The road transport corporation (RTC) of a city wants to know whether a particular bus-route is running on profit or loss.

# Assume that the following information are given:
# Price per litre of fuel = 70
# Mileage of the bus in km/litre of fuel = 10
# Price(Rs) per ticket = 80
# The bus runs on multiple routes having different distance in kms and number of passengers.
# Write a function to calculate and return the profit earned (Rs) in each route. Return -1 in case of loss.

#lex_auth_012693816779112448160

def calculate(distance,no_of_passengers):
    fuel_price = 70
    mileage = 10
    pt = 80
    c = (pt*no_of_passengers)-(distance/mileage)*fuel_price
    if c<0:
        return -1
    return c
    #Remove pass and write your logic here



#Provide different values for distance, no_of_passenger and test your program
distance=20
no_of_passengers=50
print(calculate(distance,no_of_passengers))