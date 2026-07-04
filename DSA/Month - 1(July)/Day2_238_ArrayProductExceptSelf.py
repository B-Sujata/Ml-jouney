# This is the brute force approach I used for this problem but it won't be submitted on leetcode as it's time complexity is O(n^2)so leetcode will give time limite exceeded error so I need to optimize this solution now


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        answer = []
        
        for i in range(len(nums)):
            left_product = 1
            right_product = 1
            for j in nums[:i]:
                left_product = left_product*j
            for k in nums[i+1:]:
                right_product = right_product*k
            final_product = left_product*right_product
            answer.append(final_product)
        return answer
            

# So I tried optimizing it and here I come with a different approach which uses O(n) time and space

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [0]*n
        right = [0]*n
        left[0] = 1
        right[-1] = 1
        answer = [0]*n

        for i in range(1,len(nums)):
            left[i] = left[i-1]*nums[i-1]
        for i in range(n-2, -1, -1):
            right[i] = right[i+1]*nums[i+1]
        
        for i in range(len(nums)):
            final_answer = left[i]*right[i]
            answer[i]=final_answer


        
        return answer

    
# 📝 Product of Array Except Self
# 💡 Approach
# Create two arrays:
# left to store the product of all elements to the left of each index.
# right to store the product of all elements to the right of each index.
# Initialize:
# left[0] = 1 because there are no elements to the left of the first element.
# right[n-1] = 1 because there are no elements to the right of the last element.

# Traverse the array from left to right and build the left array using the previously computed product.

# left[i] = left[i-1] * nums[i-1]

# Traverse the array from right to left and build the right array using the previously computed product.

# right[i] = right[i+1] * nums[i+1]

# Traverse the array once more and multiply the corresponding elements of the left and right arrays.

# answer[i] = left[i] * right[i]
# Return the answer array.
# 📝 Algorithm

# Step 1: Let n = len(nums).

# Step 2: Create three arrays:

# left of size n
# right of size n
# answer of size n

# Step 3: Initialize

# left[0] = 1
# right[n-1] = 1

# Step 4: Build the left product array.

# For i from 1 to n-1
#     left[i] = left[i-1] × nums[i-1]

# Step 5: Build the right product array.

# For i from n-2 down to 0
#     right[i] = right[i+1] × nums[i+1]

# Step 6: Compute the final answer.

# For i from 0 to n-1
#     answer[i] = left[i] × right[i]

# Step 7: Return answer.

# 📝 Intuition

# Instead of recalculating the product of all elements except the current element for every index (which leads to repeated computations), we store the cumulative product from both directions.

# The left array stores the product of all elements before each index.
# The right array stores the product of all elements after each index.

# The product of these two values gives the required answer for every index.

# 📝 Time Complexity

# Building the left array:

# O(n)

# Building the right array:

# O(n)

# Building the final answer:

# O(n)

# Overall Time Complexity:

# O(n) + O(n) + O(n)

# Ignoring constant factors,

# ✅ Time Complexity = O(n)
# 📝 Space Complexity

# We create three arrays of size n:

# left
# right
# answer

# Therefore,

# ✅ Space Complexity = O(n)
# 🌟 Things We Learned While Solving This Problem

# This is the part I'm happiest about because it's your reasoning process, not just the final answer.

# We first solved the problem using brute force (O(n²)).
# We noticed we were recomputing the left and right products repeatedly.
# We realized repeated computation could be avoided by storing previous results.
# We derived the prefix (left) and suffix (right) product arrays ourselves.
# We learned how to traverse an array in reverse using:
# for i in range(n-2, -1, -1):
# Finally, we combined the prefix and suffix products to obtain the answer for each index.
        


### Final optimized solution using O(1) space -- Leetcode follow up optimization

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [0]*n
        answer[0] = 1
        right_product = 1

        for i in range(1,len(nums)):
            answer[i] = answer[i-1]*nums[i-1]
        for i in range(n-2, -1, -1):
            right_product = right_product*nums[i+1]
            answer[i] = answer[i]*right_product
        
        
        return answer

        
    
    
# 📝 Product of Array Except Self (Optimized Solution)
# 💡 Approach

# Instead of maintaining separate left and right arrays, we optimize the space by using the output array itself to store the left products.

# Create an answer array of size n.
# Store the product of all elements to the left of each index directly in the answer array.
# Initialize a variable right_product = 1 to represent the product of all elements to the right of the current index.
# Traverse the array from right to left.
# For every index:
# Multiply the current left product stored in answer[i] with right_product.
# Update right_product by multiplying it with the current element of the array.
# Return the answer array.

# This eliminates the need for separate left and right arrays while maintaining the same time complexity.

# 📝 Algorithm
# Step 1

# Let

# n = length of nums

# Create an output array answer of size n.

# Initialize:

# answer[0] = 1
# right_product = 1
# Step 2

# Build the left products inside the answer array.

# For every index from 1 to n-1:

# answer[i] = answer[i-1] × nums[i-1]

# Now answer[i] stores the product of all elements to the left of index i.

# Step 3

# Traverse the array from right to left.

# For every index from n-2 to 0:

# Update the right product.
# right_product = right_product × nums[i+1]
# Multiply the stored left product with the current right product.
# answer[i] = answer[i] × right_product
# Step 4

# Return the answer array.

# 📝 Intuition

# The product of all elements except the current element can be written as:

# (Product of elements on the left)
# ×
# (Product of elements on the right)

# Instead of storing both left and right products in separate arrays:

# We store the left products directly inside the output array.
# While traversing from right to left, we maintain only one variable (right_product) that stores the cumulative product of elements to the right.

# At every index, multiplying the stored left product with the current right product gives the required answer.

# Since only one variable is used for the right product, the extra space is reduced from O(n) to O(1).

# 📝 Time Complexity
# Building left products
# O(n)
# Traversing from right to left
# O(n)

# Overall Time Complexity:

# O(n) + O(n)

# Ignoring constant factors,

# ✅ Time Complexity = O(n)
# 📝 Space Complexity

# Additional memory used:

# One variable right_product
# Loop variables (i, n)

# The answer array is not counted as extra space because it is the required output of the problem.

# Therefore,

# ✅ Extra Space Complexity = O(1)
# 🌟 Key Insight (The "Aha!" Moment)

# The biggest realization in this optimization was:

# The left products need to be stored for every index, so we store them directly in the output array.
# The right products do not need to be stored for every index. During the reverse traversal, we only need the current cumulative right product.

# So instead of:

# left[]  → stored in answer[]
# right[] → replaced by one variable (right_product)

# This simple observation reduces the auxiliary space from O(n) to O(1) while keeping the time complexity O(n).

