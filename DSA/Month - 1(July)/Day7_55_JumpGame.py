# This is how my first attempt look like, I know I have not added some conditions here yet, like instead of taking whole just taking less steps

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n==1:
            return True
        for i in range(n):
            i = i+nums[i]
            if i==n-1:
                return True
            elif i<n-1:
                i=i+nums[i]
                if i==n-1:
                    return True
            else:
                break
        return False
                

# 2nd attempt

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dist = n-1
        if n==1:
            return True
        
        while dist!=0:
            for i in range(n):
                if nums[i]==dist:
                    return True
                dist = (n-1)-i
                steps = dist - nums[i]
                if steps==nums[steps]:
                    return True
                else:
                    pass
        
        return False
                
# 3rd attempt
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest_reachable_index = 0
        n = len(nums)
        last_index = n-1
        if n==1:
            return True

        for i in range(len(nums)):
            if farthest_reachable_index<i:
                return False
            if (i+nums[i])>farthest_reachable_index:
                farthest_reachable_index= i+nums[i]
            
            if farthest_reachable_index>=last_index:
                return True
        return False
        

'''
Approach

The idea is to keep track of the farthest index that can be reached while traversing the array.

Initially, we are at index 0, so the farthest reachable index is also 0.
Traverse the array from left to right.
Before processing any index, check if the current index is reachable.
If the current index is greater than the farthest reachable index, it means we can never reach this position, so return False.
Otherwise, update the farthest reachable index if jumping from the current index allows us to reach farther.
If at any point the farthest reachable index becomes greater than or equal to the last index, return True because the destination is reachable.
If the traversal completes without reaching the last index, return False.
Algorithm
Initialize farthest_reachable_index = 0.
Find the last index of the array.
If the array contains only one element, return True.
Traverse the array from index 0 to n-1.
If the current index is greater than the farthest reachable index, return False.
Update the farthest reachable index if i + nums[i] is greater than the current farthest reachable index.
If the farthest reachable index is greater than or equal to the last index, return True.
If the loop ends without reaching the last index, return False.
Time Complexity
O(n)
We traverse the array only once.
Every operation inside the loop takes constant time.

Therefore,

O(n)
	​

Space Complexity
O(1)
We only use a few variables:
farthest_reachable_index
last_index
i
No extra data structures are used.

Therefore,

O(1)
	​

🌟 Why is this a Greedy Algorithm?

At every index, we make the locally optimal decision by updating the farthest index we can reach. We never reconsider previous choices or explore multiple paths. By always maintaining the maximum reachable index so far, we can determine whether the last index is reachable in a single traversal.


'''




        

