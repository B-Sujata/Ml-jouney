class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = []
        negative = []
        result = []

        for num in nums:
            if num>=0:
                positive.append(num)
            else:
                negative.append(num)
            
        for i in range(len(positive)):
            result.append(positive[i])
            result.append(negative[i])
        
        return result

'''
Approach

Separate the elements of nums into two arrays: one containing all positive elements and the other containing all negative elements. Since the elements are added in their original order, their relative order is preserved. Then construct the result by alternately taking one element from the positive array and one from the negative array.

Algorithm
Initialize three empty arrays: positive, negative, and result.
Traverse through nums:
If the element is positive, add it to positive.
Otherwise, add it to negative.
Traverse through the positive array:
Append positive[i] to result.
Append negative[i] to result.
Return result.
Complexity
Time Complexity: O(n)
We traverse the input and construct the result in linear time.
Space Complexity: O(n)
The positive, negative, and result arrays require linear extra space.
'''