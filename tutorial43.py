def dec_to_binary(Num):
    binary_number = ""  
    while Num > 0:
        remainder = Num % 10 
        binary_number = str(remainder) + binary_number
        Num = Num // 10 
    return binary_number if binary_number else "0" 
Num = 15 
print(dec_to_binary(Num))  
