# This is how my first attemp looke like, And guess what it passed almost 320 test cases out of umm 1000, I mean not bad for the first attempt

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        count = 0
        substring = set()

        if s == " ":
            return 1
        if len(s)==1:
            return 1
        
        for ch in s:
            if ch not in substring:
                substring.add(ch)
                count+=1
                if count>length:
                    length = count
            else:
                substring.clear()
                count = 0

        return length
    
# A fresh 2nd Attempt

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        count =0
        left = 0
       
        substring = set()

        if s == "":
            return 0
        if len(s)==1:
            return 1
        
        for index, ch in enumerate(s):
            if ch not in substring:
                substring.add(ch)
                
                diff = index -left+1
                if diff>length:
                    length = diff
            else:
                while ch in substring:
                    substring.remove(s[left])
                    left = left+1
                substring.add(ch)
                diff = index -left+1
                if diff>length:
                    length = diff
                

        return length

        
'''

Approach
Use the Sliding Window technique with two pointers (left and right).
Maintain a set to store the unique characters currently present in the window.
Traverse the string using the right pointer.
If the current character is not present in the set:
Add it to the set.
If the current character is already present:
Continuously remove characters from the left side of the window and move the left pointer forward until the duplicate character is removed.
Add the current character back to the set.
After each iteration, calculate the current window length (right - left + 1) and update the maximum length if needed.
Return the maximum length obtained.
Algorithm
Initialize:
left = 0
maxLength = 0
An empty set substring.
Traverse the string using right from 0 to n-1.
While the current character already exists in the set:
Remove the character at left from the set.
Increment left.
Add the current character to the set.

Compute the current window length as:

right - left + 1
Update maxLength if the current window length is greater.
After traversing the entire string, return maxLength.
Time Complexity
Each character is added to the set at most once and removed at most once.
Both left and right pointers traverse the string only once.

Overall Time Complexity: O(n)

Space Complexity
The set stores only the unique characters present in the current window.
In the worst case (all characters are unique), the set stores n characters.

Overall Space Complexity: O(n)


'''


        