class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_list = set(nums)
        n = len(unique_list)
        i = 0
        while i<n-1:
            if nums[i]==nums[i+1]:
                duplicate = nums.pop(i)
                nums.append(duplicate)
            else:
                i+=1
        return n

'''
Approach
Create a set from nums to find the number of unique elements.
Store this count in n.
Use a while loop to examine adjacent elements only within the first n positions.
If two adjacent elements are equal, remove the duplicate using pop(i) and append it to the end of the list.
If the adjacent elements are different, increment i.
Since duplicates are moved to the end, the first n positions eventually contain all unique elements.
Return n, the number of unique elements.
Algorithm
Create unique_list = set(nums).
Set n = len(unique_list).
Initialize i = 0.
While i < n - 1:
If nums[i] == nums[i+1]:
Remove nums[i].
Append the removed element to the end.
Do not increment i, because the new element at index i still needs to be checked.
Otherwise, increment i.
Return n.
Time Complexity

O(n²) in the worst case.

Why? pop(i) from the middle of a Python list takes O(n) because the remaining elements have to shift. This can happen multiple times.

Creating the set also takes O(n), but the repeated pop() operations dominate.

Space Complexity

O(n)

Because:

unique_list = set(nums)

stores up to n unique elements.

Final
Complexity	Your Code
Time	O(n²)
Space	O(n)
'''

# But this is not the optimal solution for this problem, In my next attempt I will try to reach at the optimal solution
