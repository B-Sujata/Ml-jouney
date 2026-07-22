# This is how my first attemp look like but while solving this I realized that for signned number, the minus sign is also reversed in this approach and hence this is not a valid solution

class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)[::-1]
        i = int(s)
        return i
        
# This is my second approach and I kid u not I thought a lot and grinded so much to reach this acceptable solution

class Solution:
    def reverse(self, x: int) -> int:
        y = 0
        result = []
        if x==0:
            return 0
        if x<0:
            sign = '-'
            x = abs(x)
        else:
            sign = ""

    
        while(x!=0):
            y = x%10
            x = x//10
            result.append(y)
            
            
        number = int("".join(map(str, result)))
        if sign == '-':
            if number in range((pow(-2, 31)),(pow(2, 31)-1)):
                return -number
        else:
            if number in range((pow(-2, 31)),(pow(2, 31))):
                return number
        return 0
    

# Attempt 3

class Solution:
    def reverse(self, x: int) -> int:
        y = 0
        answer = 0
        if x==0:
            return 0
        if x<0:
            sign = '-'
            x = abs(x)
        else:
            sign = ""

    
        while(x!=0):
            y = x%10
            x = x//10
            answer = answer*10+y
            
        if sign == '-':
            answer = -answer
        
        if answer in range((pow(-2, 31)),(pow(2, 31))):
                return answer
        return 0
    
    
        

'''
Approach
If the input number is 0, directly return 0.
Check whether the number is negative. If it is, store its sign and convert it to its absolute value.
Traverse through each digit of the number using modulo (% 10) and integer division (// 10).
Build the reversed number mathematically by shifting the current answer one place to the left (answer * 10) and adding the extracted digit.
After all digits are processed, restore the negative sign if the original number was negative.
Finally, check whether the reversed integer lies within the 32-bit signed integer range. If it does, return it; otherwise, return 0.
Algorithm
If x == 0, return 0.
Check whether x is negative.
If yes, store the sign and convert x to its absolute value.
Initialize answer = 0.
While x is not 0:
Extract the last digit using x % 10.
Remove the last digit using x // 10.

Update the reversed number using:

answer = answer * 10 + digit
Restore the negative sign if the original number was negative.
If the reversed number lies within the 32-bit signed integer range [-2³¹, 2³¹ - 1], return it.
Otherwise, return 0.
Time Complexity
O(log₁₀ n)

Reason:

In every iteration, one digit is removed from the number using integer division (x //= 10).
Therefore, the loop runs once for each digit.
A number with d digits has d = log₁₀(n) + 1 digits.

Hence, the time complexity is:

O(log₁₀ n)

Space Complexity
O(1)

Reason:

Only a constant number of variables are used:
answer
digit (y)
sign
No extra data structures such as arrays, lists, stacks, or recursion are used.

Therefore, the space complexity is:

O(1)



'''
    

# Honestly when I first saw this question I was like it's such a easy question I'll solve it in a line only but from that to coming on this solution, Ohh my god, I really really grind myself a lot but yeah honestly I leant a lot of things while solviing this problem and I'm proud of myself for that...
