

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = 0
        max_sum = nums[0]
        
        for i in range(len(nums)):
            current_sum = current_sum + nums[i]

            if current_sum>max_sum:
                max_sum = current_sum

            if current_sum<0:
                current_sum = 0
                
            
            
        return max_sum

                

        
# 📝 Maximum Subarray
# 💡 Approach
# Initialize two variables:
# current_sum to store the sum of the current subarray.
# max_sum to store the maximum subarray sum found so far.
# Traverse the array from left to right.
# Add the current element to current_sum.
# Update max_sum if current_sum is greater than the maximum found so far.
# If current_sum becomes negative, reset it to 0 because carrying a negative sum will only decrease the sum of any future subarray.
# Continue this process until the end of the array.
# Return max_sum.
# 📝 Algorithm

# Step 1: Initialize

# current_sum = 0
# max_sum = nums[0]

# Step 2: Traverse the array.

# For every element in nums:

#     Add the current element to current_sum.

#     If current_sum is greater than max_sum,
#         update max_sum.

#     If current_sum becomes negative,
#         reset current_sum to 0.

# Step 3: Return max_sum.

# 📝 Intuition

# The main idea is that a negative running sum can never help a future subarray.

# Suppose the running sum becomes:

# -8

# and the next element is

# 5

# Continuing the previous subarray gives:

# -8 + 5 = -3

# Starting a new subarray gives:

# 5

# Clearly, starting fresh is always better.

# Therefore, whenever the running sum becomes negative, we discard it and begin a new subarray from the next element.

# Meanwhile, we continuously keep track of the largest subarray sum found so far.

# 📝 Time Complexity

# The array is traversed only once.

# Therefore,

# ✅ Time Complexity = O(n)
# 📝 Space Complexity

# Only two variables are used:

# current_sum
# max_sum

# No additional arrays or data structures are created.

# ✅ Space Complexity = O(1)
# 🌟 What is Kadane's Algorithm?

# Kadane's Algorithm is an efficient dynamic programming algorithm used to find the maximum sum of a contiguous subarray in O(n) time.

# The key idea is simple:

# Keep track of the best subarray ending at the current index (current_sum).
# Keep track of the best subarray seen anywhere (max_sum).
# If the current running sum becomes negative, discard it because it cannot improve any future subarray.

# Instead of checking every possible subarray (which takes O(n²)), Kadane's Algorithm makes one decision at every element:

# Should I continue the previous subarray, or should I start a new one from here?

# That single decision is what reduces the time complexity to O(n).

# 🌟 The Biggest Lesson from This Problem

# I actually think the biggest thing you learned wasn't Kadane's Algorithm itself.

# It was this pattern:

# Stock Problem: "What is the minimum price I've seen so far?"
# Product Except Self: "What information can I store so I don't recompute products?"
# Maximum Subarray: "Should I continue the current subarray, or is it better to start a new one?"

# In all three problems, the breakthrough came from asking:

# "What is the minimum amount of information I need to remember to make the next decision?"

# That's a powerful way to approach DSA problems.