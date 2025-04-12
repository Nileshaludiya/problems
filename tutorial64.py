def find_substring(s):
    sub_string = []
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            sub_string.append(s[i:j])
    print(sub_string)
text = input("Enter a string: ")
find_substring(text)





#