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
                
