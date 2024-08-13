"""
*The flight ticket rates for a round-trip (Mumbai->Dubai) were as follows: 
*Rate per Adult: Rs. 37550.0 
*Rate per Child: 1/3rd of the rate per adult 
*Service Tax: 7% of the ticket amount (including all passengers) 
*As it was a holiday season, the airline also offered 10% discount on the final ticket cost (after inclusion of the service tax).

TODO Find and display the total ticket cost for a group which had adults and children.

#?Test the program with different input values for number of adults and children.

Sample Input:    

Number of adults  :   5                                          |||         Number of adults  :   3
Number of children:   2                                          |||         Number of children:   1
Expected Output   :  Total Ticket Cost: 204910.35                |||         Expected Output   :  Total Ticket Cost:  120535.5

"""



# #lex_auth_01269361601342668881
# def calculate_total_ticket_cost(no_of_adults, no_of_children):
#     total_ticket_cost=0
#     #Write your logic here

#     return total_ticket_cost


# #Provide different values for no_of_adults, no_of_children and test your program
# total_ticket_cost=calculate_total_ticket_cost(1,2)
# print("Total Ticket Cost:",total_ticket_cost)



def calculate_total_ticket_cost(no_of_adults, no_of_children):
    # Total_ticket_cost = 0
    adult = no_of_adults*37550.0
    child = no_of_children*(37550.0/3)
    ticket_cost = (adult + child)
    tax = (7/100)*ticket_cost
    final_ticket_cost = ticket_cost + tax
    Total_ticket_cost = final_ticket_cost - ((10/100)*final_ticket_cost)
    return Total_ticket_cost

total_ticket_cost= calculate_total_ticket_cost(3,1)
print("Total Ticket Cost:",total_ticket_cost)




def calculate_total_ticket_cost(no_of_adults, no_of_children):
    # Total_ticket_cost = 0
    ticket_cost = (no_of_adults*37550.0 + no_of_children*(37550.0/3))
    service_tax = ticket_cost + (7/100)*ticket_cost
    Total_ticket_cost = service_tax - ((10/100)*service_tax)
    return Total_ticket_cost

total_ticket_cost= calculate_total_ticket_cost(3,1)
print("Total Ticket Cost",format(total_ticket_cost))



