'''Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.'''


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq = {0:0, 1:0, 2:0}
        for value in nums:
            if value in freq:
                freq[value]+=1
            else:
                freq[value] = 1
        
        for i in range(freq[0]):
            nums[i]=0

        for i in range(freq[0], freq[0]+freq[1]):
            nums[i]=1
        
        for i in range(freq[0]+freq[1], len(nums)):
            nums[i]=2
    


'''
Sort Colors — Counting/Frequency Approach
Approach

Use a dictionary to count how many times each color (0, 1, 2) appears in the array.

Then use these frequencies to overwrite the original array in sorted order:

Put all 0s at the beginning.
Put all 1s immediately after the 0s.
Put all 2s in the remaining positions.

The array is modified in-place, so we don't create another array.

Algorithm

Initialize a frequency dictionary:

freq = {0: 0, 1: 0, 2: 0}
Traverse nums and count the occurrences of each value.
Fill the first freq[0] positions with 0.
Fill the next freq[1] positions with 1, starting from index freq[0].

Fill all remaining positions with 2, starting from:

freq[0] + freq[1]
Since nums is modified directly, nothing needs to be returned.
Example
nums = [2, 0, 2, 1, 1, 0]

Frequency:

0 → 2
1 → 2
2 → 2

Then overwrite:

0 0 | 1 1 | 2 2

Result:

[0, 0, 1, 1, 2, 2]
Complexity

Time Complexity: O(n)

One traversal to count the elements → O(n)
Three loops to rewrite the array → O(n)
Overall → O(n)

Space Complexity: O(1)

The dictionary contains only three keys (0, 1, 2), regardless of how large n becomes.

So your solution is:

Time: O(n)
Space: O(1)

Now we've got your first approach properly understood. ❤️

Next, the Dutch National Flag approach is interesting because instead of:

"Count first → overwrite later"

we'll try to think:

"Can I arrange the 0s, 1s and 2s while I'm traversing the array?"

That's where the three pointers come in. 🧠🔥

'''

# Dutch National Flag solution
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = 0
        mid = 0
        high = len(nums)-1

        while mid<=high:
            if nums[mid]==1:
                mid+=1
            elif nums[mid]==2:
                nums[mid], nums[high] = nums[high], nums[mid]
                high-=1
            else:
                nums[mid], nums[low]= nums[low], nums[mid]
                mid+=1
                low+=1


'''
Sort Colors — Dutch National Flag Approach
Approach

Use three pointers — low, mid, and high — to divide the array into four regions:

[ 0s | 1s | unknown | 2s ]
       ↑      ↑        ↑
      low    mid      high
low keeps track of where the next 0 should go.
mid checks the current element.
high keeps track of where the next 2 should go.

As we examine each element:

If it is 0, swap it toward the left.
If it is 1, leave it where it is and move mid.
If it is 2, swap it toward the right.

The important trick is that when we encounter 2, we do not move mid, because the element swapped from the right hasn't been checked yet.

Algorithm

Initialize three pointers:

low = 0
mid = 0
high = len(nums) - 1

Continue while:

mid <= high

Check nums[mid]:

If nums[mid] == 0:

Swap nums[mid] with nums[low].
Increment low.
Increment mid.

If nums[mid] == 1:

It is already in the correct middle region.
Increment mid.

If nums[mid] == 2:

Swap nums[mid] with nums[high].
Decrement high.
Do not increment mid, because the newly swapped element needs to be checked.
Continue until mid > high.

The array is now sorted as:

0s → 1s → 2s
Complexity
Time Complexity: O(n)

Each element is processed a constant number of times.

So for n elements:

O(n)

Space Complexity: O(1)

We only use three variables:

low
mid
high

No extra array, dictionary, or other data structure is needed.

O(1)

Final complexity
	Complexity
Time	O(n)
Space	O(1)

This is the optimal/canonical solution for this problem. 🔥
'''