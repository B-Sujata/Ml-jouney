num = (input("Enter a number:"))



def oct(num):
    pairs = {0:'000', 1:'001', 2:'010', 3:'011', 4:'100', 5:'101', 6:'110', 7:'111'}
    binary = ""
    for digit in num:
        binary+=pairs[int(digit)]
    
    return binary

print(oct(num))