class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = []
        
        for index, val in enumerate(nums):
            s = target - val
            if s in nums:
                for i,num in enumerate(nums):
                    if num==s:
                        if i!=index:
                            indices.append(index)

                
                

                


                    

                
                
                    

                
                
        
            
        
        
        