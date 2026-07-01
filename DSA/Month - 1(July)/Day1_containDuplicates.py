
nums = [1,2, 3, 4, 1, 5, 2]
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        s = set(nums)  # It takes O(n) time
        if len(s)==len(nums): # takes O(1) + O(1) + O(1)
            return False
        else:
            return True

solution = Solution()
print(solution.containsDuplicate(nums))
        
'''
Time Complexity - O(n)
Space Complexity - O(n)
'''
        
         
        