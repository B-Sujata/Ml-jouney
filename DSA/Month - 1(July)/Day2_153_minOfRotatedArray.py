class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n-1
        
        while(left<right):
            if nums[left]<nums[right]:
                return nums[left]
            else:
                mid = (left+right)//2

                if nums[left]<=nums[mid]:
                    left = mid+1
                else:
                    right = mid
        return nums[left]
                
                
                

# Find Minimum in Rotated Sorted Array (Binary Search)
# Approach

# The array is originally sorted in ascending order but rotated at an unknown pivot. Instead of finding the rotation count, we use the sorted property of the array to eliminate half of the search space in every iteration.

# Initialize two pointers, left and right, at the beginning and end of the array.
# While left < right:
# If the current search space is already sorted (nums[left] < nums[right]), then the first element of that search space is the minimum. Return nums[left].
# Find the middle index mid.
# If the left half (left to mid) is sorted (nums[left] <= nums[mid]):
# The minimum cannot be in this sorted left half, so search the right half by updating left = mid + 1.
# Otherwise, the right half is sorted.
# Since mid itself could be the minimum, keep it in the search space by updating right = mid.
# When the loop ends, left and right point to the same element, which is the minimum. Return nums[left].
# Algorithm

# Initialize:

# left = 0
# right = len(nums) - 1
# Repeat while left < right:
# If nums[left] < nums[right], return nums[left].

# Compute:

# mid = (left + right) // 2
# If nums[left] <= nums[mid]:

# Update:

# left = mid + 1
# Else:

# Update:

# right = mid

# Return:

# nums[left]
# Time Complexity
# O(log n)

# Reason:

# In every iteration, half of the search space is discarded.
# The search interval keeps shrinking by approximately half until only one element remains.
# Therefore, the number of iterations is logarithmic.
# Space Complexity
# O(1)

# Reason:

# We only use a few variables (left, right, and mid).
# No extra array or recursion is used.
# 🌟 Most Important Insight (the one you discovered)

# Binary Search is not about finding the answer directly.

# It is about identifying which half cannot possibly contain the answer and discarding it.

# That's exactly the mindset we developed today.