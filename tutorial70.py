text = '8765432123'
result = 0
for i in text:
    int_value = ord(i) - ord("0")
    result = result*10+int_value
print(result)
