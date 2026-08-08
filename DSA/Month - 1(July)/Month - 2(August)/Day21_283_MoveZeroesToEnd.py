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