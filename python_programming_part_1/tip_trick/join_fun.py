list1 = ['g', 'e', 'e', 'k', 's']
print("".join(list1)) # geeks



str = '-'.join('hello')
print(str)  # Output: h-e-l-l-o



words = ["apple", "", "banana", "cherry", ""]
separator = "@ "
result = separator.join(word for word in words if word)
print(result) 



list1 = {'1', '2', '3', '4', '4'} 
s = "-#-"
s = s.join(list1)
print(s)
