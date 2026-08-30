class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = [nums[0]]
        arr2 = [nums[1]]
        for num in nums[2:]:
            if arr1[-1]>arr2[-1]:
                arr1.append(num)
            else:
                arr2.append(num)
        
        return arr1+arr2

        return result

'''
Approach

Use two arrays, arr1 and arr2, and distribute the elements according to the last elements of the two arrays. If the last element of arr1 is greater than the last element of arr2, add the current element to arr1; otherwise, add it to arr2. Finally, concatenate both arrays.

Algorithm
Initialize arr1 with nums[0] and arr2 with nums[1].
Traverse the remaining elements of nums starting from index 2.
For each element:
If arr1[-1] > arr2[-1], append it to arr1.
Otherwise, append it to arr2.
Concatenate arr1 and arr2.
Return the resulting array.
Complexity
Time Complexity: O(n) — each element is processed once.
Space Complexity: O(n) — arr1 and arr2 together store all n elements.

'''