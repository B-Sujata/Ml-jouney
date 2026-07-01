'''
Approach
Iterate through every element of the array.
For each element, compute the value required to reach the target.
Search the entire array to find that required value.
Ensure that the same index is not used twice.
As soon as a valid pair is found, return both indices because the problem guarantees exactly one solution.

'''

## The solution is not the best or optimized efficient I know, But I learnt a lot of things while solving this problem and I am proud that I found out the solution on my own after getting so many errors, after my code failing so many times, this is the brute force approach I discovered and in future as I learn more things, I will optimize my solution

nums = [2,7,3,4]
target = 5

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        indices = []
        
        for index, val in enumerate(nums):
            s = target - val
            if s in nums:
                for i,num in enumerate(nums):
                    if num==s:
                        if i!=index:
                            indices.append(index)
                            indices.append(i)
                            return indices

solution = Solution()

print(solution.twoSum(nums, target))       
    


'''
Algorithm (Brute Force)
Create an empty list indices.
Traverse the list using enumerate() to get the current index and value.

For each element, calculate its complement:

complement = target - current_value
Traverse the list again to search for the complement.
If the complement is found and its index is different from the current index:
Store both indices.
Return the list of indices immediately.
If no valid pair is found, the function ends (though in the Two Sum problem, it is guaranteed that one valid pair exists).


'''

'''
Time Complexity
Outer loop: O(n)
Inner loop: O(n)
Overall: O(n²)
Space complexity: O(2)
'''

                        

                
                

                


                    

                
                
                    

                
                
        
            
        
        
        
                
                
                    

                
                
        
            
        
        
        