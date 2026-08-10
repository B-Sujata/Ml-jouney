class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count =0
        max_count = 0

        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
            else:
                if count>max_count:
                    max_count = count
                count = 0
            
            if count>max_count:
                max_count = count
        return max_count

'''
Approach

Use a counter to keep track of the current consecutive sequence of 1s and a max_count variable to store the longest sequence found so far.

Whenever the current element is 1, increase count.
Whenever the current element is 0, the current sequence ends, so compare count with max_count and reset count to 0.
After each iteration, compare count and max_count to make sure a sequence of 1s at the end of the array is also considered.
Algorithm
Initialize count = 0 and max_count = 0.
Traverse every element of the array.
If the current element is 1:
Increment count.
If the current element is 0:
Compare count with max_count.
Update max_count if count is greater.
Reset count to 0.
After each iteration, compare count with max_count.
Return max_count.
Time Complexity

O(n)

The array is traversed only once.

Space Complexity

O(1)

Only two variables, count and max_count, are used regardless of the input size.

Final
Complexity	Value
Time	O(n) ✅
Space	O(1) ✅

'''