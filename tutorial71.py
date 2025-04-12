# def frequence_char(s):
#     result = {}
#     count = 0
#     for i in s:
#         for j in s:
#             if i == j:
#                 count += 1
#         result[i] = count
#         count = 0
#         # print(result[i])
#         max_value = max(result)
#         # print(max_value)
#         # print(result.items())
#         f_char = [key for key,value in result.items() if value == max_value]
#         print(f_char)        

# text = input("Enter a string: ")
# frequence_char(text)


def count_letter(text):
    file = {}
    for x in text:
        if x in file:
            file[x] += 1
        else :
            file[x] = 1   
    file_all = file
    max_value = max(file_all.values())
    f_char =  [key for key,value in file_all.items() if value == max_value]
    print(f_char)
text = input("Enter a string: ")
count_letter(text)