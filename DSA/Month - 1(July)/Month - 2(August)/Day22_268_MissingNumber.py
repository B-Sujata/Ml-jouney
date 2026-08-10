class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        if nums[0]!=0:
            return 0
        for num in range(len(nums)-1):
            if nums[num+1]-nums[num]==1:
                continue
            else:
                return nums[num]+1
        return nums[-1]+1    

        


'''
Approach
First, sort the array in ascending order.
Since the numbers should contain all values from 0 to n except one, check whether 0 is missing.
Traverse the sorted array and compare every pair of consecutive elements.
If the difference between two consecutive numbers is greater than 1, the missing number is nums[i] + 1.
If no number is missing in between, then the missing number must be the number immediately after the last element.
Algorithm
Sort the given array.
Check if the first element is not 0.
If yes, return 0.
Iterate through the array from the first element to the second-last element.
For each pair of consecutive elements:
If nums[i+1] - nums[i] == 1, continue.
Otherwise, return nums[i] + 1.
If the loop completes, return nums[-1] + 1.
Time Complexity

O(n log n)

Sorting takes O(n log n).
Traversing the array takes O(n).
Therefore, overall:

O(n log n)

Space Complexity

O(1) auxiliary space

The array is sorted in-place, and no additional data structure proportional to n is used.

Note: Depending on the Python sorting implementation, the internal sorting operation can use temporary memory, but for algorithm-analysis purposes, this solution is generally described as O(1) auxiliary space when treating sort() as in-place.

Short version for your notes

Approach: Sort the array and find the gap between consecutive numbers. If 0 is missing, return 0. If no gap exists, the missing number is the next number after the last element.

Time: O(n log n)
Space: O(1) auxiliary space

'''

# Optimal Solution using XOR operation

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        result = n

        for i in range(n):
            result^=i^nums[i]
        return result


'''
Approach

Use the XOR operation to find the missing number without sorting the array.

The array should contain every number from 0 to n, but exactly one number is missing.

XOR has an important property:

x ^ x = 0
x ^ 0 = x

Therefore, if we XOR all numbers from 0 to n with all the numbers present in the array, every number that exists in both sets will cancel out. The only number left will be the missing number.

Algorithm
Find n, which is the length of the array.
Initialize result with n.
This accounts for the last number in the range 0 to n.
Traverse the array using index i.
For every index, XOR:
the index i
the corresponding array element nums[i]
After all elements are processed, all duplicate numbers cancel each other through XOR.
The remaining value is the missing number.
Return result.
Code
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        result = n

        for i in range(n):
            result ^= i ^ nums[i]

        return result
Time Complexity

O(n)

We traverse the array exactly once.

n elements → one pass → O(n)
Space Complexity

O(1)

We only use a few variables (n, result, i) and don't create any additional data structure.

⭐ Final Summary
	Complexity
Time	O(n) ✅
Space	O(1) ✅

So this is an optimal solution for the Missing Number problem in terms of time and auxiliary space. 🎯
'''