num = (input("Enter a number:"))



def oct(num):
    pairs = {0:'000', 1:'001', 2:'010', 3:'011', 4:'100', 5:'101', 6:'110', 7:'111'}
    binary = ""
    for digit in num:
        if int(digit)>=0 and int(digit)<=7:
            binary+=pairs[int(digit)]
        else:
            return "Invalid octal Number"

        
    
    return binary

print(oct(num))