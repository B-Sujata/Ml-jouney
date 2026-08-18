# I solved it in 4 minutes only 😁
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}
        lst = []
        n = len(nums)
        majority = n/3
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num] = 1
            if freq[num]>majority:
                if num not in lst:
                    lst.append(num)
        return lst
            
'''
Approach

Use a frequency dictionary to keep track of how many times each element appears in the array. Whenever the frequency of an element becomes greater than n/3, add that element to the result list if it is not already present.

Algorithm
Initialize an empty dictionary freq to store the frequency of each element.
Initialize an empty list lst to store the majority elements.
Calculate n = len(nums) and the threshold n/3.
Traverse every element num in nums:
If num is already present in freq, increment its frequency.
Otherwise, initialize its frequency to 1.
If its frequency becomes greater than n/3 and it is not already in lst, add it to lst.
Return lst.
Complexity

Time Complexity: O(n)

You traverse the array once. Dictionary lookup, insertion, and update take O(1) average time.

Space Complexity: O(n)

In the worst case, all n elements can be distinct, so the frequency dictionary can contain n entries.

Final
Approach: Frequency counting using a dictionary
Time: O(n)
Space: O(n)
'''

# Optimal Solution

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate1 = nums[0]
        candidate2 = None
        lst = []
        count1 = 0
        count2 = 0
        majority = len(nums)//3
        freq1 = 0
        freq2 = 0
        for num in nums:
        
            if num==candidate1:
                count1+=1
                
            elif num==candidate2:
                count2+=1
                
            elif count1==0:
                candidate1 = num
                count1+=1
            elif count2==0 and num!= candidate1:
                candidate2 = num
                count2+=1
            else:
                count1-=1
                count2-=1
        
        for num in nums:
            if num==candidate1:
                freq1+=1
            elif num==candidate2:
                freq2+=1
            else:
                continue
        if freq1>majority:
            lst.append(candidate1)
        if freq2>majority:
            lst.append(candidate2)
        return lst
            
        
'''
Approach

Use the Boyer-Moore Voting Algorithm with two candidates because there can be at most two elements that appear more than n/3 times.

Maintain two candidates (candidate1, candidate2) and their voting counts. During the first pass, cancel the votes of elements that are different from both candidates. This leaves at most two potential majority candidates.

Since the voting counts are not their actual frequencies, perform a second pass to count the actual occurrences of both candidates and return those whose frequency is greater than n/3.

Algorithm
Initialize two candidates and their counts.
Traverse the array:
If num equals candidate1, increment count1.
Else if num equals candidate2, increment count2.
Else if count1 == 0, make num the new candidate1.
Else if count2 == 0, make num the new candidate2.
Otherwise, decrement both count1 and count2.
Traverse the array again and count the actual frequencies of candidate1 and candidate2.
If either frequency is greater than n//3, add that candidate to the result.
Return the result.
Complexity
Time Complexity: O(n) — two passes through the array.
Space Complexity: O(1) — only a constant number of variables are used.

'''