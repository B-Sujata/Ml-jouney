# It feels good to derive the solution all on your own and get in accepted in the first 2 attempts without any errors, this was what I could think of in the first place

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        majority = n//2
        freq={}

        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        for i,j in freq.items():
            if j>majority:
                return i
            
        
