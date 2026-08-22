class Solution:
    def checkDivisibility(self, n: int) -> bool:
        original_num = n
        digits_sum = 0
        digits_product = 1

        while(n!=0):
            digits_sum+=n%10
            digits_product*=n%10
            n = n//10
        
        divisor = digits_sum+digits_product
        
        if original_num%divisor==0:
            return True
        return False

    
'''
Approach
Store the original value of n because n will be modified while extracting its digits.
Extract each digit using n % 10.
Maintain:
digits_sum → sum of all digits.
digits_product → product of all digits.
Remove the last digit using n // 10.
Calculate the divisor as:
digits_sum + digits_product
Finally, check whether the original number is divisible by this divisor.
Algorithm
Store n in original_num.
Initialize digits_sum = 0 and digits_product = 1.
While n is not zero:
Extract the last digit using n % 10.
Add it to digits_sum.
Multiply it with digits_product.
Remove the last digit using n // 10.
Calculate divisor = digits_sum + digits_product.
Check if original_num % divisor == 0.
If yes, return True; otherwise, return False.
Complexity
Time Complexity: O(log₁₀ n) — each digit of n is processed exactly once.
Space Complexity: O(1) — only a constant number of variables are used.

'''