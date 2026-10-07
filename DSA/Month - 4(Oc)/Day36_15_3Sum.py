class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n-2):
            if nums[i]>0:
                break
            if i>0 and nums[i]==nums[i-1]:
                continue
            l = i +1
            r = n-1
            while l<r:
                sum = nums[i]+nums[l]+nums[r]
                if sum<0:
                    l+=1
                elif sum>0:
                    r-=1
                else:
                    result.append([nums[i], nums[l], nums[r]] )
                    l+=1
                    r-=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1

        return result

'''
Approach
The code uses the Sorting + Two Pointer approach.
1. Sort the array so that elements are in increasing order.
2. Fix one element using i.
3. For every fixed i, use two pointers:
   - l = i + 1 → starts just after i
   - r = n - 1 → starts at the end
4. Calculate:sum = nums[i] + nums[l] + nums[r]
5. Based on the sum:
   - If sum < 0 → increase l to get a larger value.
   - If sum > 0 → decrease r to get a smaller value.
   - If sum == 0 → store the triplet and move both pointers.
6. Skip duplicate values for i and l to avoid duplicate triplets.
7. Stop early when nums[i] > 0, because with a sorted array, three numbers cannot sum to zero after that point.
Algorithm
1. Sort nums.
2. Initialize result = [].
3. For i from 0 to n-3:
      a. If nums[i] > 0, stop.
      b. If nums[i] == nums[i-1], skip this i.
      c. Set l = i + 1 and r = n - 1.
      d. While l < r:
            i. Calculate sum = nums[i] + nums[l] + nums[r].
           ii. If sum < 0, increment l.
          iii. If sum > 0, decrement r.
           iv. If sum == 0:
                - Add the triplet to result.
                - Increment l and decrement r.
                - Skip duplicate values of l.
4. Return result.

Complexity
Time Complexity: O(n²)
- Sorting: O(n log n)
- Outer loop + two-pointer traversal: O(n²)
- Overall: O(n²)
Space Complexity: O(1) auxiliary space
Apart from the result list, the algorithm uses only a constant amount of extra space.
So:
Time: O(n²)
Auxiliary Space: O(1)
Output Space: O(k), where k is the number of triplets returned.

'''