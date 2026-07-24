# After spending hours on this problem I finally come up with a solution whose sample test cases are accepted but it can't be submitted on leetcode and I learned here where comes the Sieve of Eratosthenes algorithm. And Leetcode problem number 204 is to teach this Sieve of Eratosthenes algorithm so Yess Now I'll again start from the scratch and solve this problem by this approach and I'm determined to get it submitted on the leetcode today itself.Let's go we've got this one...

class Solution:
    def countPrimes(self, n: int) -> int:
        count = 0
        
        if n==0 or n==1:
            return 0
        if 2<n:
            count+=1
        
        for num in range(3, n, 2):
            divisor_found = False
            for i in range(3, int(math.sqrt(num))+1, 2):
                if num%i==0:
                    divisor_found = True
                    break
            if divisor_found==False:
                count+=1
        return count


# And finally after struggling for so long, here's the solution
class Solution:
    def countPrimes(self, n: int) -> int:
        if n==0 or n==1:
            return 0
        nums=[True]*n
        nums[0]=False 
        nums[1]=False

        for i in range(2, int(math.sqrt(n))+1):
            if nums[i]==True:
                for j in range(i*i, n, i):
                    nums[j]=False
        return nums.count(True)





        


'''
Algorithm Name

Sieve of Eratosthenes

Approach
Assume that every number from 2 to n-1 is prime by creating a boolean array nums and initializing all values to True.
Mark 0 and 1 as False since they are not prime.
Traverse from 2 to √n.
If the current number is still marked as prime (True), mark all of its multiples (starting from i × i) as False because they cannot be prime.
After all multiples have been marked, count the remaining True values in the array. These represent all prime numbers less than n.
Algorithm
If n is 0 or 1, return 0.
Create a boolean array nums of size n and initialize all elements as True.
Mark nums[0] and nums[1] as False.
Traverse from 2 to √n.
For every number i:
If nums[i] is True, it is a prime number.
Mark all multiples of i starting from i × i as False.
Count all the True values in the array.
Return the count.
Why do we start from i × i?

All smaller multiples of i (such as 2 × i, 3 × i, ..., (i-1) × i) have already been marked while processing smaller prime numbers.

For example:

For i = 5

10 was marked while processing 2
15 was marked while processing 3
20 was marked while processing 2

So the first multiple that still needs to be marked is:

5 × 5 = 25

This avoids unnecessary work and improves efficiency.

Time Complexity
O(n log log n)
Explanation
The outer loop runs only up to √n.
The inner loop runs only for prime numbers.
Each composite number is marked only a limited number of times.
The total work performed by the algorithm is approximately O(n log log n), making it much faster than checking every number individually.
Space Complexity
O(n)
Explanation

A boolean array of size n is used to keep track of whether each number is prime or not.

Key Observations
✔ Initially, assume every number is prime.
✔ Skip numbers that have already been marked as non-prime.
✔ Start marking multiples from i × i.
✔ Only iterate up to √n.
✔ Count the remaining True values to get the answer.

This is the standard and most efficient solution for LeetCode 204 - Count Primes and is widely expected in coding interviews.

'''
        
        
        
