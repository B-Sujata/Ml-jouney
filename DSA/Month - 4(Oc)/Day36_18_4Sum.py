class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n-3):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1, n-2):
                
                
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                l = j+1
                r = n-1
                while l<r:
                    if nums[i]+nums[j]+nums[l]+nums[r]<target:
                        l+=1
                    elif nums[i]+nums[j]+nums[l]+nums[r]>target:
                        r-=1
                    else:
                        result.append([nums[i], nums[j], nums[l], nums[r]])
                        l+=1
                        r-=1
                        while l<r and nums[l]==nums[l-1]:
                            l+=1
        return result


'''
Approach
The code uses Sorting + Two Nested Loops + Two Pointers.
1. Sort the array.
2. Fix the first element using i.
3. Fix the second element using j.
4. Use two pointers:
   - l = j + 1
   - r = n - 1
5. Calculate the sum of the four elements:nums[i] + nums[j] + nums[l] + nums[r]
6. Since the array is sorted:
   - If sum < target → move l right.
   - If sum > target → move r left.
   - If sum == target → add the quadruplet and move both pointers.
7. Skip duplicate values for i, j, and l to avoid duplicate quadruplets.
Algorithm
1. Sort nums.
2. Initialize result = [].
3. For i from 0 to n-4:
      a. Skip duplicate nums[i].
      b. For j from i+1 to n-3:
            i. Skip duplicate nums[j].
           ii. Set l = j+1 and r = n-1.
          iii. While l < r:
                - Calculate sum of nums[i], nums[j], nums[l], nums[r].
                - If sum < target:
                      l++
                - If sum > target:
                      r--
                - If sum == target:
                      Add quadruplet to result.
                      l++
                      r--
                      Skip duplicate nums[l].
4. Return result.

Complexity
Time Complexity: O(n³)
- Sorting: O(n log n)
- i loop: O(n)
- j loop: O(n)
- Two-pointer traversal: O(n)
Therefore:
O(n × n × n) = O(n³)
Space Complexity: O(1) auxiliary space
The algorithm itself uses constant extra space apart from the output.
Output space: O(k), where k is the number of quadruplets returned.
Final
Complexity	Value
Time	O(n³)
Auxiliary Space	O(1)
Output Space	O(k)
'''