## First Attemp

class Solution:
    def check(self, nums: List[int]) -> bool:
        if nums==sorted(nums):
            return True
        i =0
        
        while i<len(nums)-1:
            nums= nums[1:]+ [nums[0]]
            if nums==sorted(nums):
                return True
            else:
                i = i+1

        return False

    '''
    Approach

The idea is to check whether the given array can become sorted after performing one or more left circular rotations.

First, check if the array is already sorted. If yes, return True.
Otherwise, repeatedly perform a left rotation by moving the first element to the end.
After each rotation, compare the rotated array with its sorted version.
If at any point the rotated array becomes sorted, return True.
If all possible rotations are exhausted without obtaining a sorted array, return False.
Algorithm
If nums is already sorted, return True.
Initialize a counter i = 0.
While i < len(nums) - 1:

Perform one left rotation:

nums = nums[1:] + [nums[0]]
If the rotated array is sorted, return True.
Otherwise, increment i.
Return False.
Time Complexity

Let n be the size of the array.

sorted(nums) takes O(n log n).

A single rotation using slicing:

nums[1:] + [nums[0]]

takes O(n).

The loop runs at most n − 1 times.

Therefore,

Time Complexity = O(n × (n log n + n)) = O(n² log n)

Space Complexity
sorted(nums) creates a new sorted list of size n.
The rotation operation also creates a new list of size n.

At any given moment, the extra memory used is proportional to the input size.

Space Complexity = O(n)
    
    
    '''