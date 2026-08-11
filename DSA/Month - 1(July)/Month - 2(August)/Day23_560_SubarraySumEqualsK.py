# First Attempt --- The samples cases ran but some of the test cases fail and i understood the problem why

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        if len(nums)==1:
            if sum(nums)==k:
                count+=1
        else:
            if k in nums:
                count+=1
            if sum(nums)==k:
                count+=1
            
            for num in range(len(nums)-1):
                if nums[num]+nums[num+1]==k:
                    count+=1
            
        return count

 # Second Attempt

 class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        array_sum = 0
        if len(nums)==0:
            return 0
        
        if len(nums)==1:
            if sum(nums)==k:
                count+=1
        else:
            if k in nums:
                count+=1
            # if sum(nums)==k:
            #     count+=1
            
            for num in range(len(nums)):
                if array_sum<k:
                    array_sum+=nums[num]
                else:
                    array_sum = 0
                
                if array_sum==k:
                    count+=1
                
            
        return count


# Third attempt - I am solving this problem from last 1 and half hour and I finally reached on a valid solution using brute force but it's time complexity goes till O(n^2) and leetcode accepted solution is O(n) so my code passes only 83 test cases out of 93 and now I'll have to think about some better approach for this problem

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        
        if len(nums)==0:
            return 0
        
        if len(nums)==1:
            if sum(nums)==k:
                count+=1
        else:
            if k in nums:
                count+=1
            # if sum(nums)==k:
            #     count+=1
            
            for num in range(len(nums)):
                array_sum = 0
                for j in range(num, len(nums)):
                    array_sum+=nums[j]
                    
                    
                    if array_sum==k:
                        count+=1
                
            
        return count

'''
Approach

The idea is to consider every possible starting position of a subarray and then extend the subarray one element at a time.

For each starting index, we maintain a running sum (array_sum). Whenever this sum becomes equal to k, we increment count.

The nested loops ensure that all possible contiguous subarrays are checked.

Algorithm
Initialize count = 0.
Handle the empty-array case.
Handle the single-element case separately.
For every index num:
Reset array_sum = 0.
Start another loop from num to the end of the array.
Add each element to array_sum.
If array_sum == k, increment count.
Return count.
Complexity

Time Complexity: O(n²)

The outer loop runs n times.
For each starting position, the inner loop can run up to n times.
Therefore, in the worst case:
O(n × n) = O(n²)

Space Complexity: O(1)

We only use a few variables such as count and array_sum. No additional data structure whose size depends on n is used.

In one line

Brute force: Generate every possible contiguous subarray using two loops, calculate its sum incrementally, and count the ones whose sum equals k.


'''

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        count = 0
        freq = {0:1}

        for num in nums:
            prefix_sum+=num
            
            count+=freq.get(prefix_sum-k, 0)

            if prefix_sum in freq:
                freq[prefix_sum]+=1
            else:
                freq[prefix_sum]=1
        return count


'''
Approach

Instead of generating every possible subarray like the brute-force approach, we use a prefix sum to keep track of the cumulative sum while traversing the array once.

For every current prefix sum, we check whether we have previously seen:

current prefix sum - k

If we have, the difference between the current prefix sum and that previous prefix sum is exactly k, meaning a valid subarray exists.

A dictionary freq stores:

prefix_sum → number of times that prefix_sum has occurred

The frequency is important because the same prefix sum can occur multiple times, and each occurrence can represent a different valid subarray.

Algorithm
Initialize:
prefix_sum = 0
count = 0
freq = {0: 1}
Traverse the array from left to right.
For every element:
Add the element to prefix_sum.

Calculate:

prefix_sum - k
Check how many times this required prefix sum has appeared in freq.
Add that frequency to count.
Store the current prefix_sum in freq by increasing its frequency.
Return count.
Why freq = {0: 1}?

It represents a prefix sum of 0 before the array starts.

This allows us to correctly count subarrays that start from index 0.

Time Complexity
O(n)

We traverse the array only once.

Dictionary lookup and insertion are O(1) on average.

Therefore:

O(n)

This is a major improvement over the brute-force O(n²) approach.

Space Complexity
O(n)

In the worst case, every prefix sum can be different, so the dictionary can contain up to n entries.

Therefore:

O(n)
Comparison with your brute-force approach
Approach	Time	Space
Brute Force	O(n²)	O(1)
Prefix Sum + Frequency Dictionary	O(n)	O(n)
One-line summary

Traverse the array once using prefix sums, and use a frequency dictionary to determine how many previous prefix sums can form a subarray with sum k.
'''
        