def remove_repeat_character(s):
    x = 0
    for i in s:
        if s.index(i) == x:
            print(i,end="")
        x += 1
text = input("Enter a string: ")
remove_repeat_character(text)