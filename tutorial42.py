def decimal_to_binary(Num):
    binary_number = ""
    while Num > 0:
        remainder = Num % 2  
        binary_number = str(remainder) + binary_number
        Num = Num // 2 
    return binary_number if binary_number else "0" 

Num = int (input("Enter a number: ")) 
print(decimal_to_binary(Num),"This is binary number of the",Num)
    