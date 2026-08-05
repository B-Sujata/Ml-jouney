# First attemot --> The logic is corrrect but for leetcode submission it's not efficient, it passes 39 out of 41 test cases and gives TLE error so need to try something else now

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        rotated_nums = nums.copy()
        k = k%len(nums)
        
        
        while(k>0):
            rotated_nums = [rotated_nums[-1]]+rotated_nums[:-1]
            k-=1
        nums.clear()
        nums.extend(rotated_nums)

'''
Approach

Create a copy of the original array and perform the right rotation one step at a time. In each iteration, move the last element to the front and keep the remaining elements in their original order. Repeat this process k times (after reducing k using modulo). Finally, clear the original array and extend it with the rotated array so that the modification is done on the original list.

Algorithm
Create a copy of the original array.
Compute k = k % len(nums) to eliminate unnecessary full rotations.
Repeat the following k times:
Move the last element of the copied array to the front.
Append the remaining elements after it.
Clear the original array.
Extend the original array with the rotated array.
Time Complexity
Creating the copy → O(n)
k %= len(nums) → O(1)

Each rotation:

rotated_nums = [rotated_nums[-1]] + rotated_nums[:-1]

takes O(n).

Performed k times.

Overall Time Complexity: O(n × k)
(After modulo, this can also be written as O(n × (k % n)).)

Space Complexity
Copy of the array → O(n)
Each rotation creates a temporary list of size n, but only one exists at a time.

Overall Space Complexity: O(n)

'''
        

# OPtimal Solution --> 2nd attempt, I can't believe the optimal solution was just 4 lines of code, here it is

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        k = k%len(nums)
        nums.reverse()
        nums[:k]=nums[:k][::-1]
        nums[k:] = nums[k:][::-1]
            
        
        
'''
Approach

Instead of shifting the array one position at a time, use the Reverse Array technique. First, reduce unnecessary rotations by taking k % len(nums). Then, reverse the entire array, which brings the last k elements to the front but in reverse order. Next, reverse the first k elements to restore their correct order, and finally reverse the remaining n-k elements to restore the order of the remaining elements. This results in the required right-rotated array.

Algorithm
Compute k = k % len(nums) to avoid unnecessary full rotations.
Reverse the entire array.
Reverse the first k elements.
Reverse the remaining n-k elements.
The array is now rotated to the right by k positions.
Time Complexity
k %= len(nums) → O(1)
nums.reverse() → O(n)
nums[:k] = nums[:k][::-1] → O(k)
nums[k:] = nums[k:][::-1] → O(n - k)

Overall:

Time Complexity: O(n)

Space Complexity
Using Python slicing ([::-1]) creates temporary lists for the slices.
The total extra memory used is proportional to the size of the array.

Space Complexity: O(n)

Note: If the subarrays were reversed in place using the two-pointer technique instead of slicing, the space complexity would become O(1) while keeping the time complexity O(n).

'''

# Third attempt -- optimal solution

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        k = k%len(nums)
        nums.reverse()
        
        def reverse(nums, left, right):
            while(left<right):
                nums[left], nums[right] = nums[right], nums[left]
                left+=1
                right-=1
            
        reverse(nums, 0, k-1)
        reverse(nums, k, len(nums)-1)
            
        
        


'''
Approach

Instead of shifting the array one position at a time, use the Reverse Array technique. First, reduce unnecessary rotations by computing k % len(nums). Then, reverse the entire array. This brings the last k elements to the front, but in reverse order. Next, reverse the first k elements to restore their correct order, and finally reverse the remaining n-k elements to restore the order of the remaining elements. This rotates the array to the right by k positions while modifying it in place.

Algorithm
Compute k = k % len(nums) to eliminate unnecessary full rotations.
Define a helper function reverse(nums, left, right) that reverses the elements between the given indices using the two-pointer approach.
Reverse the entire array.
Reverse the first k elements.
Reverse the remaining n-k elements.
The array is now rotated to the right by k positions.
Time Complexity
Reverse the entire array → O(n)
Reverse the first k elements → O(k)
Reverse the remaining n-k elements → O(n - k)

Overall:

Time Complexity: O(n)

Space Complexity

The algorithm performs all reversals in place using only two pointers (left and right) and does not create any extra arrays.

Space Complexity: O(1)


'''