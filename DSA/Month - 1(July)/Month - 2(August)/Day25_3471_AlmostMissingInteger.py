# First Attempt -- This passed 600 cases out of 900 btw, I mean still feels like an achivement

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)-1
        # if k==1:
        #     return max(nums)
        if nums[0]==nums[n]:
            return -1
        elif nums[0]>nums[n]:
            if nums[0] not in nums[1:]:
                return nums[0]
            else:
                return nums[n]
        else:
            if nums[n] not in nums[1:n]:
                return nums[n]
            else:
                return nums[0]
        

# Acceptable solution

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        
        subarray_count1 = 0
        subarray_count2 = 0
        n = len(nums)-1
        total_subarrays = len(nums)-k+1
        candidate = -1
        if k==len(nums):
            return max(nums)
        if k==1:
            for num in nums:
                if nums.count(num)==1:
                    if num>candidate:
                        candidate = num
            return candidate
        
        

        for i in range(total_subarrays):

            if nums[0] in nums[i:i+k]:
                subarray_count1+=1
            if nums[n] in nums[i:i+k]:
                subarray_count2+=1
        if subarray_count1==1 and subarray_count2==1:
            return max(nums[0], nums[n])
        elif subarray_count1>1 and subarray_count2==1:
            return nums[n]
        elif subarray_count1==1 and subarray_count2>1:
            return nums[0]
        else:
            return -1





'''
Approach

The solution handles three cases:

k == len(nums)
There is only one subarray, which is the entire array.
Therefore, every distinct element appears in exactly one subarray.
Return the maximum element.
k == 1
Every element itself forms a separate subarray.
Therefore, an element appears in exactly one subarray iff it occurs exactly once in nums.
Find the largest element whose frequency is 1.
1 < k < len(nums)
Only the first element and last element can belong to exactly one subarray.
Check all possible subarrays of size k and count how many subarrays contain:
nums[0]
nums[-1]
If both occur in exactly one subarray, return the larger one.
If only one occurs exactly once, return that one.
Otherwise, return -1.
Algorithm
Let n = len(nums) - 1.
If k == len(nums), return max(nums).
If k == 1:
For every num in nums, check nums.count(num).
If its count is 1, update the largest candidate.
Return the candidate.
Otherwise:
Calculate the number of size-k subarrays: len(nums) - k + 1.
For every valid starting index i:
Consider nums[i:i+k].
Check whether it contains nums[0].
Check whether it contains nums[n].
Compare the two counts.
Return the appropriate candidate or -1.
Complexity

For your exact implementation:

Case	Time	Space
k == len(nums)	O(n)	O(1)
k == 1	O(n²)	O(1)
1 < k < n	O(nk)	O(k)

The general case is O(nk) because there are O(n) subarrays, and each nums[i:i+k] creates a slice of size k and performs membership checking.

Overall

Worst-case time complexity: O(nk)
Worst-case auxiliary space: O(k)
'''