def sum(num):
    if(num == 1):
        return 1
    return num + sum(num-1)
num = int(input("Enter a number: "))
print(sum(num))
