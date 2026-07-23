### I solved this problem in my first attemp in 5 minutes 49 seconds, I am so proud of myself, Below is my solution

class Solution:
    def isPalindrome(self, x: int) -> bool:
        original_val= x
        answer = 0
        if x ==0:
            return True
        if x<0:
            return False
        while(x!=0):
            y = x%10
            x = x//10
            answer = answer*10+y
        if original_val == answer:
            return True
        return False
        
