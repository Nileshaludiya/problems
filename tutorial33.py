T = int(input("Enter value of T: "))
reversed = 0
for i in range(T):
    remainder = T % 10
    reversed = reversed + remainder
    T = int(T/10)
print(reversed)        
