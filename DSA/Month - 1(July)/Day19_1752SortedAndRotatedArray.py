# First attempt

class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(len(nums)-1):
            if nums[i]<=nums[i+1]:
                return True
            nums[i], nums[n-1-i] = nums[n-1-i], nums[i]
            if nums ==nums.sort():
                return True
        return False
        