def print_list(list,idx):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)
fruits = ['mangos','litchi','apple','banana']
print_list(fruits,0)    