def longest_world(text):
    list1 = text.split()
    print(list1)
    return max(list1)
text = input("Enter a string: ")
print(longest_world(text))