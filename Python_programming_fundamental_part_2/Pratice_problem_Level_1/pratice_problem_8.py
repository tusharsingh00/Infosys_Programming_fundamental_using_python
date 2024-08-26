""" 
Write a python function which accepts a list of strings containing details of deposits and withdrawals made in a bank account and returns the net amount in the account.

Suppose the following input is supplied to the function 
["D:300","D:300","W:200","D:100"] where D means deposit and W means withdrawal,
then the net amount in the account is 500.

Sample Input
["D:300","D:200","W:200","D:100"]
["D:350","W:100","W:500","D:1000"]

Expected Output
400
750

""" 

#lex_auth_0127135929511936001157

def calculate_net_amount(trans_list):
    net_amount =0
    for i in trans_list:
        if i[0] == "D":
            net_amount += int(i[2:len(i)])
        else:
            net_amount -= int(i[2:len(i)])
    return(net_amount)


trans_list=["D:300","D:200","W:200","D:100"]
print(calculate_net_amount(trans_list))

