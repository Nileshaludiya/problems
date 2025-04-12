def search_substring(s,s1):
     return s1 in s           
str1 = input("Enter a string: ")
str2 = input("Enter substring: ")
print(search_substring(str1,str2))