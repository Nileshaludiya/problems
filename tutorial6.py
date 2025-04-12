# Write a program to input three numbers(A, B & C) from user and print the maximum element among A, B & C in each line.		
# Problem Constraints		
# 1 <= A <= 1000000		

a = float(input("Enter first number :"))
b = int(input("Enter second number :"))
c = float(input("Enter third number :"))
if(a>=b and a>=c):
    print("greatest number a",a)
elif(b>=c):
    print("greatest number b :",b)
else:
    print("greatest number c :",c)    