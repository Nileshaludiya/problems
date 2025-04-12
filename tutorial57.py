def check_palindrome(s):
    a = s[::-1]
    if s == a:
        print(True)
    else :
        print(False)
str1 = input("Enter a string: ")
check_palindrome(str1)