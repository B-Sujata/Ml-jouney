# Guess What I Solved this problem all on my own in just 10 mins, First time solving recursion, I'm so happieee

class Solution:
    def fib(self, n: int) -> int:
        
        if n==0:
            return 0
        elif n == 1:
            return 1
        return self.fib(n-1)+self.fib(n-2)


'''
Overall Analysis

Approach: Recursive (Top-Down without memoization)

Algorithm:

If n == 0, return 0.
If n == 1, return 1.
Otherwise, recursively compute fib(n-1) and fib(n-2).
Return their sum.

Time Complexity: O(2^n)

Space Complexity: O(n)


'''

            
# THis is not an optimal solution