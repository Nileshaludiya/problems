# def frequent_char(s):


# s = int(input("Enter a string: "))
# frequent_char(s)
def make_pattern():
    alfabat = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(N):
        print("")
        for j in range(i+1):
            print(alfabat[i], end=" ")
N = int(input("enter a number :"))   
make_pattern()         