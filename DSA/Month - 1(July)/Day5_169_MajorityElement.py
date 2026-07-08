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
            
# Then after this, to optimize this , I learnt about a very cool algorithm called "Boyer–Moore Voting Algorithm" and this was my code after that

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        count = 0

        for num in nums:
            if count==0:
                candidate=num
            if num==candidate:
                count+=1
            else:
                count-=1 
            
        return candidate
        

'''
Solution 1: Using Frequency Dictionary (Hash Map)
Approach

The majority element is the element that appears more than ⌊n/2⌋ times in the array.

To find it, we use a dictionary (hash map) to store the frequency of every element while traversing the array. Once the frequency of each element is known, we iterate through the dictionary and return the element whose frequency is greater than ⌊n/2⌋.

This approach is simple and efficient because dictionary operations (insertion and lookup) take O(1) time on average.

Algorithm
Calculate the majority frequency as n // 2.
Create an empty dictionary to store the frequency of each element.
Traverse the array:
If the element already exists in the dictionary, increment its count.
Otherwise, insert it into the dictionary with frequency 1.
Traverse the dictionary:
If any element's frequency is greater than n // 2, return that element.
Time Complexity

O(n)

First traversal of the array: O(n)
Second traversal of the dictionary: O(k), where k is the number of distinct elements.
In the worst case, every element is unique, so k = n.

Therefore,

Time Complexity = O(n + n) = O(n)

Space Complexity

O(n)

In the worst case, every element in the array is unique.

Example:

[1,2,3,4,5]

The dictionary stores all five elements.

Hence,

Space Complexity = O(n)



'''


'''
Solution 2: Boyer-Moore Voting Algorithm
Approach

The Boyer-Moore Voting Algorithm is based on the observation that the majority element appears more than half of the time.

We maintain two variables:

candidate → stores the current potential majority element.
count → stores the balance of votes for the current candidate.

While traversing the array:

If count becomes 0, we choose the current element as the new candidate.
If the current element matches the candidate, we increase the count.
Otherwise, we decrease the count, effectively canceling one occurrence of the candidate with one occurrence of a different element.

Since the majority element appears more than all other elements combined, it can never be completely canceled out and will remain as the final candidate.

Algorithm
Initialize:
candidate as the first element.
count = 0.
Traverse each element in the array.
If count == 0, make the current element the new candidate.
If the current element equals the candidate:
Increment count.
Otherwise:
Decrement count.
After traversing the array, return the candidate.
Time Complexity

O(n)

The array is traversed only once, and each operation inside the loop takes constant time.

Therefore,

Time Complexity = O(n)

Space Complexity

O(1)

Only two extra variables are used:

candidate
count

No additional data structures are required.

Therefore,

Space Complexity = O(1)

💡 Why Boyer-Moore Works (Intuition)

Imagine every occurrence of the majority element cancels out one occurrence of a different element.

For example:

2 2 2 1 1

Cancel one 2 with one 1:

2 2 1

Cancel another 2 with another 1:

2

The majority element still survives because it initially appeared more than all other elements combined.

This is why repeatedly increasing and decreasing the count eventually leaves the majority element as the final candidate.

'''
