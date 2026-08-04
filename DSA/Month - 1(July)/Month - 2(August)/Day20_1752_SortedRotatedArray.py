## First Attemp

class Solution:
    def check(self, nums: List[int]) -> bool:
        if nums==sorted(nums):
            return True
        i =0
        
        while i<len(nums)-1:
            nums= nums[1:]+ [nums[0]]
            if nums==sorted(nums):
                return True
            else:
                i = i+1

        return False