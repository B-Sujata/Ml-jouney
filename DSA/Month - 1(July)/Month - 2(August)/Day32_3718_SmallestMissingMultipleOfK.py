class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        for i in range(1, len(nums)+2):
            if k*i not in nums:
                return k*i
        

'''
Approach

The goal is to find the smallest positive multiple of k that is not present in nums.

We start checking multiples of k one by one:

k, 2k, 3k, 4k, ...

For each multiple k * i, we check whether it exists in nums. As soon as we find a multiple that is not present, we return it.

We only need to check up to len(nums) + 1 multiples because nums contains only len(nums) elements, so at least one of these multiples must be missing.

Algorithm
Iterate i from 1 to len(nums) + 1.
Calculate the current multiple k * i.
Check if k * i is present in nums.
If it is not present, return k * i.
The loop is guaranteed to find a missing multiple.
Time Complexity

O(n²) in the worst case.

The loop runs at most O(n) times.
Searching k * i in a list takes O(n) time.
Therefore: O(n × n) = O(n²).
Space Complexity

O(1) auxiliary space.

We don't create any additional data structure whose size depends on n.

So the final complexity is:

Complexity	Value
Time	O(n²)
Space	O(1)

Note: If you convert nums to a set, the same approach can be optimized to O(n) time with O(n) space.
'''
# Optimal Solution
class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums_set = set(nums)
        for i in range(1, len(nums_set)+2):
            if k*i not in nums_set:
                return k*i
        
'''
Approach

Use a set to store all elements of nums. A set allows us to check whether an element exists in O(1) average time.

Then, check the multiples of k one by one:

k, 2k, 3k, 4k, ...

The first multiple that is not present in the set is the answer.

We only need to check up to len(nums_set) + 1 multiples because there are only len(nums_set) distinct elements, so at least one of the first len(nums_set) + 1 multiples must be missing.

Algorithm
Convert nums into a set.
Iterate i from 1 to len(nums_set) + 1.
Calculate the current multiple k * i.
Check whether k * i exists in the set.
If it does not exist, return k * i.
Time Complexity
Creating the set: O(n)
Checking the multiples: O(n) iterations.
Each set lookup: O(1) average

Therefore:

Time Complexity: O(n) average.

Space Complexity

The set stores up to n elements.

Space Complexity: O(n)

Final
Complexity	Value
Time	O(n) average
Space	O(n)

This is the optimized version of your original O(n²) solution.
'''