
#? Given a list of integer values. Write a python program to check whether it contains same number in adjacent position. Display the count of such adjacent occurrences

"""
--------------------------------------------------------------------------------------------------------------
        sample Input                                                          Expected Output
---------------------------------------------------------------------------------------------------------------
[1,1,5,100,-20,-20,6,0,0]                          ||                               3
[10,20,30,40,30,20]                                ||                               0
[1,2,2,3,4,4,4,10]                                 ||                               3
 ---------------------------------------------------------------------------------------------------------------
 
  """
  
def get_count(num_list):
    count=0
    for i in range(len(num_list)-1):
        if num_list[i+1] == num_list[i]:
            count += 1
        
    return count

#provide different values in list and test your program
num_list=[10,0,30,40,10,10]
print(get_count(num_list))