class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        while(i<len(nums)-1):
            if nums[i]!=0:
                i+=1
            elif nums[i+1]!=0:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                i+=1
            else:
                j = i+1
                while(j<len(nums)-1 and nums[j]==0 ):
                    j+=1
                if nums[j]!=0:
                    nums[i], nums[j] = nums[j], nums[i]
                    i+=1
                else:
                    break
                
                
'''Approach

Use two pointers, i and j, to move all zeroes toward the end while modifying the array in-place.

i represents the current position being processed.
If nums[i] is non-zero, it is already in the correct relative position, so move i forward.
If nums[i] is zero and the next element is non-zero, swap them and move i forward.
If there are consecutive zeroes, use a second pointer j to search ahead for the next non-zero element.
If j finds a non-zero element, swap it with the zero at i.
If no non-zero element exists after i, stop because all remaining elements are zero.

The array is modified in-place, so no additional array is required.

Algorithm
Initialize i = 0.
Continue while i is not at the last position.
If nums[i] is non-zero:
Increment i.
Otherwise, nums[i] is zero:
If nums[i+1] is non-zero, swap nums[i] and nums[i+1], then increment i.
Otherwise, initialize j = i + 1.
Move j forward while it is within the array and points to a zero.
If j points to a non-zero element:
Swap nums[i] and nums[j].
Increment i.
If no non-zero element is found, break.
The array now contains all zeroes at the end.
Complexity
Time Complexity: O(n²)

In the worst case, there can be many consecutive zeroes, and for each zero position, j may scan through a large portion of the remaining array.

Therefore, the worst-case time complexity is:

O(n²)

Space Complexity: O(1)

Only a few variables (i and j) are used. No additional array or data structure is created.

Therefore:

Space Complexity = O(1)

Final Summary
Aspect	Complexity
Time	O(n²)
Space	O(1)
Approach	Two-pointer / in-place swapping'''

#Optimal Solution

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = i+1
        while(j<len(nums)):
            if nums[i]!=0:
                i+=1
                j+=1
            else:
                if nums[j]!=0:
                    nums[i],nums[j] = nums[j], nums[i]
                    i+=1
                    j+=1
                else:
                    j+=1
            
            
                

'''
Approach

Use two pointers, i and j, to move all zeroes to the end of the array in-place.

i keeps track of the position where a zero is present and where the next non-zero element should be placed.
j scans the array ahead of i to find non-zero elements.
If nums[i] is non-zero, both pointers move forward.
If nums[i] is zero and nums[j] is non-zero, swap them and move both pointers.
If both positions contain zeroes, only j moves forward to search for the next non-zero element.

This ensures that every element is processed only once.

Algorithm
Initialize i = 0 and j = 1.
Traverse the array while j is within the array.
If nums[i] is non-zero:
Increment both i and j.
Otherwise, nums[i] is zero:
If nums[j] is non-zero:
Swap nums[i] and nums[j].
Increment both i and j.
If nums[j] is also zero:
Increment only j.
Continue until j reaches the end of the array.
The zeroes are now moved to the end while maintaining the relative order of non-zero elements.
Complexity
Time Complexity: O(n)

Both i and j only move forward through the array. Neither pointer moves backward or repeatedly scans the same elements.

Therefore:

Time = O(n)

Space Complexity: O(1)

The algorithm uses only two pointer variables and performs the swaps directly in the original array.

Therefore:

Space = O(1)

Final Summary
Aspect	Complexity
Approach	Two Pointers
Time	O(n)
Space	O(1)
Modification	In-place
Relative order of non-zero elements	Preserved

'''