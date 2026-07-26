class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False
        if n==1:
            return True
        elif n%2==0:
            return self.isPowerOfTwo(n/2)   
        return False   

'''
Approach

The idea is to repeatedly divide the number by 2 until it becomes 1.

If n is less than or equal to 0, it cannot be a power of 2, so return False.
If n becomes 1, it means the original number was obtained by repeatedly multiplying 2, so return True.
If n is divisible by 2, recursively check whether n / 2 is also a power of 2.
If n is not divisible by 2 (except when it is 1), it cannot be a power of 2, so return False.
Algorithm
If n <= 0, return False.
If n == 1, return True.
If n is divisible by 2:
Recursively call isPowerOfTwo(n // 2).
Otherwise, return False.
Time Complexity

Time Complexity: O(log n)

Explanation:

At every recursive call, the value of n is divided by 2.

For example:

64 → 32 → 16 → 8 → 4 → 2 → 1

The number of times a value can be divided by 2 before reaching 1 is approximately log₂(n).

Therefore, the time complexity is:

O(log n)

Space Complexity

Space Complexity: O(log n)

Explanation:

Since recursion is used, each recursive call is stored in the function call stack.

The maximum depth of recursion is equal to the number of times n can be divided by 2, which is log₂(n).

Therefore, the recursion stack requires:

O(log n) space.



'''