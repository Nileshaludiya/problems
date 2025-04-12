def find_frequency_cher(s):
    s = s.lower()
    for i in range(97,123):
        c = 0
        j = chr(i)
        for l in s:
            if j == l:
                c += 1        
        if c > 0:
            print( j ,":", c )      
str = input("Enter a string: ")
find_frequency_cher(str)