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

                        

# It's been a month and today I again tried solving this problem and this is what it looks like, the time complexity is still o(n^2) but I didn't need much time to solve it now, it was done in approx 5 minutes and the code looks cleaner than before so yes, This is a progress

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, value in enumerate(nums):
            sol=target - value
            if sol in nums and nums.index(sol)!=index:
                return [index, nums.index(sol)]


'''
Approach

Use a brute-force search approach. Traverse the list element by element. For each element, calculate the value required to reach the target:

required = target - current_value

Then check whether this required value exists in the list and make sure its index is different from the current index.

Algorithm
Traverse the list using enumerate() to get both index and value.
For each value, calculate:
sol = target - value
Check if sol exists in nums.
Find the index of sol using nums.index(sol).
Make sure the found index is not the current index.
If both conditions are satisfied, return the two indices.
Continue until the pair is found.
Time Complexity

O(n²)

Why?

for loop → O(n)
sol in nums → O(n)
nums.index(sol) → O(n)

These searches happen inside the loop, so overall:

O(n × n) = O(n²)

Space Complexity

O(1)

You're not creating any additional data structure whose size depends on n. Apart from a few variables like index, value, and sol, the extra space is constant.

Final:
Time: O(n²)
Space: O(1)

And yes — this is a perfectly valid brute-force solution, just not the optimal one. The dictionary version improves the time to O(n) at the cost of O(n) extra space.

'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq = {}
        for index, num in enumerate(nums):
            if target - num in freq:
                return [index, freq[target-num]]
            else:
                freq[num] = index


'''
Two Sum — Hash Map Approach
Approach

Use a dictionary (Hash Map) to store each number and its index while traversing the array.

For every number num, calculate its complement:

complement = target - num

The complement is the number we need to find so that:

num + complement = target

Before storing the current number, check whether its complement already exists in the dictionary.

If it exists → we found the two numbers, so return their indices.
If it doesn't exist → store the current number and its index in the dictionary.

The dictionary stores:

number → index
Algorithm

Create an empty dictionary:

freq = {}
Traverse nums using enumerate() to get both the index and value.

For each num, calculate:

target - num
Check whether this complement exists in freq.

If it exists:

return [current_index, freq[complement]]

Otherwise, store:

freq[num] = current_index
Continue until the required pair is found.
Example
nums = [2, 7, 11, 15]
target = 9

First:

num = 2
complement = 9 - 2 = 7

7 isn't in the dictionary, so store:

{2: 0}

Next:

num = 7
complement = 9 - 7 = 2

2 is in the dictionary:

{2: 0}

Therefore:

return [1, 0]
Complexity

Time Complexity: O(n)

We traverse the array once, and dictionary lookup is O(1) on average.

Space Complexity: O(n)

In the worst case, we may store almost every element in the dictionary.

Final
	Complexity
Time	O(n)
Space	O(n)

This is the optimal standard Hash Map solution for Two Sum. 🔥

'''                


                    

                
                
                    

                
                
        
            
        
        
        
                
                
                    

                
                
        
            
        
        
        