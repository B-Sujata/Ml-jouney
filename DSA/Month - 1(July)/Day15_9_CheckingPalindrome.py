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

## THe optimal Solution

class Solution:
    def isPalindrome(self, x: int) -> bool:
        answer = 0
        reversed_num = 0
        if x==0:
            return True
        if x<0:
            return False
        if x%10==0:
            return False
        while(x>answer):
            reversed_num= x%10
            x = x//10
            
            answer = answer*10+reversed_num
            
        if x == answer or x==answer//10:
            return True
        return False


'''
Approach

Instead of reversing the entire number, we reverse only half of the digits.

If the number is negative, it cannot be a palindrome.
If the number ends with 0 (except 0 itself), it also cannot be a palindrome because a palindrome cannot start with 0.
Repeatedly extract the last digit of the number and build the reversed second half.
Continue this process until the reversed half becomes greater than or equal to the remaining half.
For numbers with an even number of digits, both halves should be equal.
For numbers with an odd number of digits, the middle digit does not affect the palindrome property, so remove it from the reversed half using integer division (// 10) before comparing.

This approach avoids reversing the entire number, making it more efficient.

Algorithm
If the number is negative, return False.
If the number ends with 0 and is not 0, return False.
Initialize two variables:
answer = 0 (stores the reversed second half of the number)
reversed_num = 0 (stores the current extracted digit)
While the remaining number is greater than the reversed half:
Extract the last digit using % 10.
Remove the last digit from the original number using // 10.
Append the extracted digit to answer.
After the loop:
If x == answer, return True (even number of digits).
Else if x == answer // 10, return True (odd number of digits).
Otherwise, return False.
Time Complexity
O(log n)
Explanation:
In each iteration, one digit is removed from the original number using:
x = x // 10
Since a number with d digits requires d iterations to remove all digits, and this algorithm only processes about half of the digits, the loop runs approximately d / 2 times.
The number of digits in an integer n is:
log
10
	​

(n)+1

Ignoring constants in Big-O notation:

O(
2
logn
	​

)=O(logn)

Therefore, the time complexity is O(log n).

Space Complexity
O(1)
Explanation:

The algorithm uses only a constant amount of extra space:

answer
reversed_num
x

No additional data structures (arrays, lists, stacks, etc.) are used, and the amount of memory remains constant regardless of the size of the input.

Therefore, the space complexity is O(1).


'''
        
