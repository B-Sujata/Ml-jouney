## First Attemp ---> By left shift

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

# 2nd attempt --> Right shift

class Solution:
    def check(self, nums: List[int]) -> bool:
        if nums==sorted(nums):
            return True
        i =0
        
        while i<len(nums)-1:
            nums= [nums[-1]]+ nums[:-1]
            if nums==sorted(nums):
                return True
            else:
                i = i+1

        return False

'''
Algorithm
Check if nums is already sorted.
If yes, return True.
Initialize a counter i = 0.
While i < len(nums) - 1:

Perform one right rotation:

nums = [nums[-1]] + nums[:-1]
If nums == sorted(nums), return True.
Otherwise, increment i.
If no rotation results in a sorted array, return False.
Time Complexity

Let n be the number of elements in the array.

Checking sorted(nums) takes O(n log n).
One right rotation using slicing takes O(n).
The loop executes at most n − 1 times.

Therefore,

Time Complexity = O(n × (n log n + n)) = O(n² log n)

Space Complexity
sorted(nums) creates a new sorted list of size n.
The right rotation operation also creates a new list of size n.

Hence,

Space Complexity = O(n)

'''

# 3rd attempt

class Solution:
    def check(self, nums: List[int]) -> bool:
        if nums==sorted(nums):
            return True
        
        for i in range(len(nums)-1):
            
            if nums[i]<=nums[i+1]:
                continue
            else:
                left = nums[:i+1]
                right = nums [i+1:]
        if left == sorted(left) and right ==sorted(right):
            if left[0]>=right[0]:
                if right[-1]<=left[0]:
                    return True
                
            else:
                if left[-1]<=right[0]:
                    return True
        return False
        
       
            
'''
Approach
First, check if the array is already sorted. If it is, return True.
Traverse the array to find the point where the order breaks (nums[i] > nums[i+1]). This point represents the possible rotation index.
Split the array into two parts:
left = nums[:i+1]
right = nums[i+1:]
Check if both subarrays are individually sorted.
Compare the boundary elements of the two subarrays to verify that they can form a sorted array after rotation.
If all conditions are satisfied, return True; otherwise, return False.
Algorithm
If nums is already sorted, return True.
Iterate through the array:
If nums[i] <= nums[i+1], continue.
Otherwise, split the array into left and right.
Check whether both left and right are sorted.
Verify the boundary relationship between the two subarrays.
If the conditions hold, return True.
Otherwise, return False.
Time Complexity
Checking if the array is sorted:
sorted(nums) → O(n log n)
Finding the split point:
O(n)
Checking left == sorted(left):
O(n log n) (in the worst case)
Checking right == sorted(right):
O(n log n) (in the worst case)

Overall Time Complexity:

O(n log n)

Space Complexity
sorted(nums) creates a new list → O(n)
sorted(left) and sorted(right) also create new lists (overall still proportional to n).
left and right are slices, which together store n elements.

Overall Space Complexity:

O(n)

'''

# Optimal Solution

class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                count+=1
        
        if count==0:
            return True
                
        if count ==1:
            if nums[0]>=nums[-1]:
                return True
        return False

           



'''
Approach

A sorted array has no order violations, whereas a rotated sorted array has exactly one order violation. Traverse the array once and count the number of indices where the current element is greater than the next element. Since the array is circular, also compare the last element with the first element. If the total number of order violations is at most one, the array can be obtained by rotating a sorted array; otherwise, it cannot.

Algorithm
Initialize a variable count = 0.
Traverse the array from index 0 to n-2:
If nums[i] > nums[i+1], increment count.
Compare the last and first elements:
If nums[-1] > nums[0], increment count.
If count <= 1, return True.
Otherwise, return False.
Time Complexity
Single traversal of the array: O(n)
One additional comparison between the last and first elements: O(1)

Overall Time Complexity: O(n)

Space Complexity
Only one integer variable (count) is used.
No extra arrays or data structures are created.

Overall Space Complexity: O(1)

This is the optimal solution for the problem because it examines each element only once and uses constant extra space.

'''