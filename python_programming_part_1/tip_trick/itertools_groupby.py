# This method calculates the keys for each element present in iterable. It returns key and iterable of grouped items.

def encode(s):
    from itertools import groupby
    return ''.join(f"{len(list(g))}{k}" for k, g in groupby(s))
encoded_message=encode("ABBBBCCCCCCCCAB")
print(encoded_message)

# ************************************************************************


import itertools 
  
  
a_list = [("Animal", "cat"),  
          ("Animal", "dog"),  
          ("Bird", "peacock"),  
          ("Bird", "pigeon")] 
  
  
an_iterator = itertools.groupby(a_list, lambda x : x[0]) 
  
for key, group in an_iterator: 
    key_and_group = {key : list(group)} 
    print(key_and_group) 
    

# ********************************************************************************************************    
from itertools import groupby

data = "AAAABBBCCDAA"
grouped = groupby(data)

# Output: [('A', 'AAAA'), ('B', 'BBB'), ('C', 'CC'), ('D', 'D'), ('A', 'AA')]
for key, group in grouped:
    print(f"{key}: {''.join(group)}")
    
# ************************************************************************************************************
from itertools import groupby

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f"{self.name}({self.age})"

people = [
    Person("Alice", 30),
    Person("Bob", 30),
    Person("Alice", 35),
    Person("Bob", 25)
]

# Group by name
grouped = groupby(people, key=lambda p: p.name)

# Output: [ ('Alice', [Alice(30), Alice(35)]), ('Bob', [Bob(30), Bob(25)])]
for key, group in grouped:
    print(f"{key}: {list(group)}")

