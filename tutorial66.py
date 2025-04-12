def find_substring(s):
    sub_string = ""
    for i in range(len(s),0,-1):
        for j in range(len(s)+1-i):
            sub_string += s[j:i]
            print(sub_string)
            if sub_string == sub_string[::-1]:
                return sub_string
            sub_string = "" 
            j+=1
            i+=1
text = input("Enter a string: ")
print(find_substring(text))
