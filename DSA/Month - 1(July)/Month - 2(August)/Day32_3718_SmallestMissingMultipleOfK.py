

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