num = int(input("Enter a num: "))

def fac_of_num(num):
    a = 1
    for i in range(num,0,-1):
        a = a * i
    print(a)    
fac_of_num(num)