# I solved it in first attemp in 4 minutes only, Feels like an achivement...Achievement Indeed

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
            
        for key, value in freq.items():
            if value == 1:
                return key



'''
Approach

Use a frequency dictionary to count how many times each number appears in the array.

Since every number appears twice except one number, the number with a frequency of 1 is the single number.

Algorithm
Initialize an empty dictionary freq.
Traverse through the array.
For each number:
If it already exists in freq, increment its frequency.
Otherwise, add it to the dictionary with frequency 1.
Traverse through the dictionary.
Find the key whose frequency is 1.
Return that key.
Time Complexity

O(n)

First loop → O(n)
Second loop through the dictionary → O(n) in the worst case
Overall → O(n)
Space Complexity

O(n)

In the worst case, the dictionary can contain up to n distinct elements.

Final
Complexity	Value
Time	O(n) ✅
Space	O(n)


'''

# Optimal Solution

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0

        for num in nums:
            result^=num     
        return result


'''
Approach

Use the XOR operation to find the number that appears only once.

Since every other number appears exactly twice, XORing all the elements will cancel out the duplicate numbers because:

x ^ x = 0

and:

0 ^ x = x

Therefore, after XORing all elements, only the number that appears once remains.

Algorithm
Initialize result = 0.
Traverse through every number in nums.
XOR each number with result.
Duplicate numbers cancel each other out.
The remaining value in result is the single number.
Return result.
Time Complexity

O(n)

We traverse the array once.

Space Complexity

O(1)

Only one extra variable, result, is used.

Final
Complexity	Value
Time	O(n) ✅
Space	O(1) ✅
'''