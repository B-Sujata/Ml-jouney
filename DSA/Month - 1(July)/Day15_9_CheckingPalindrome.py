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

'''
Approach

The idea is to determine whether the given integer is a palindrome by reversing the entire number and comparing it with the original number.

Store the original value of the integer in a separate variable.
If the number is negative, immediately return False since negative numbers cannot be palindromes due to the minus (-) sign.
Reverse the digits of the number by repeatedly:
Extracting the last digit using the modulo (%) operator.
Removing the last digit using integer division (//).
Appending the extracted digit to the reversed number.
After the complete number has been reversed, compare it with the original number.
If both numbers are equal, return True; otherwise, return False.
Algorithm
Store the original number in original_val.
Initialize answer = 0.
If x == 0, return True.
If x < 0, return False.
Repeat until x becomes 0:

Extract the last digit:

digit = x % 10

Remove the last digit:

x = x // 10

Append the digit to the reversed number:

answer = answer * 10 + digit
Compare answer with original_val.
If they are equal, return True; otherwise, return False.
Time Complexity

Let d be the number of digits in the integer.

The while loop processes one digit during each iteration.

For example:

12321

Iteration 1 → 1
Iteration 2 → 2
Iteration 3 → 3
Iteration 4 → 2
Iteration 5 → 1

If the number contains d digits, the loop executes d times.

Since the number of digits in an integer n is:

d=⌊log
10
	​

(n)⌋+1

the overall time complexity is:

Time Complexity: O(log n)

Space Complexity

The algorithm uses only a constant amount of extra memory.

Extra variables used are:

original_val
answer
digit

No additional data structures such as arrays, lists, or strings are created.

Therefore,

Space Complexity: O(1)


'''
        
