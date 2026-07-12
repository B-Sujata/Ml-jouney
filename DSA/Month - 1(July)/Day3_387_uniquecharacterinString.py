class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        freq = {}
        
        for ch in s:
            if ch in freq:
                freq[ch]+=1
            else:
                freq[ch]=1

        for index, ch in enumerate(s):
            if freq[ch]==1:
                return index
        return -1

                





'''
LeetCode 387 - First Unique Character in a String
Approach

We create a dictionary to store the frequency of every character in the string. We traverse the string once and count how many times each character appears.

After building the frequency dictionary, we traverse the string again while keeping track of each character's index using enumerate(). Since the string preserves the original order of characters, the first character whose frequency is 1 is the first non-repeating character. We immediately return its index.

If no character has a frequency of 1, it means every character repeats, so we return -1.

Algorithm
Create an empty dictionary to store character frequencies.
Traverse the string and count the occurrence of each character.
Traverse the string again using enumerate().
For each character, check its frequency in the dictionary.
If the frequency is 1, return its index.
If no unique character is found after traversing the entire string, return -1.
Time Complexity

Let n be the length of the string.

Building the frequency dictionary takes O(n).
Traversing the string again to find the first unique character takes O(n).

Overall Time Complexity:

O(n)

Since both traversals are linear and performed sequentially, the overall time complexity remains O(n).

Space Complexity

A dictionary is used to store the frequency of each unique character.

In the worst case, when every character in the string is unique, the dictionary stores n key-value pairs.

Overall Space Complexity:

O(n)

Note: If the problem is restricted to only lowercase English letters (26 characters), the auxiliary space can be considered O(1) because the dictionary size is bounded by a constant. However, for a general string, the space complexity is O(n).

Key Learning
A dictionary is useful for counting the frequency of characters efficiently.
The dictionary provides the frequency of each character but does not preserve the original position of characters.
The original string must be traversed again to identify the first unique character.
enumerate() is useful when both the index and the value of an iterable are required.
Separate the responsibilities of your data structures:
Dictionary → Stores frequencies.
String → Preserves the original order of characters.
Why We Traverse the String Twice

During the first traversal, we determine how many times each character appears.

During the second traversal, we identify the first character whose frequency is 1.

A single traversal is not sufficient because, when a character is encountered for the first time, we cannot know whether it will appear again later in the string.

Final Solution Analysis
Approach	Time Complexity	Space Complexity
Frequency Dictionary + Second Traversal	O(n)	O(n)
Why This Solution is Optimal
Every character must be examined at least once, so the minimum possible time complexity is O(n).
The algorithm achieves this lower bound, making it asymptotically optimal.
Using a frequency dictionary allows each character lookup to be performed in constant time on average, resulting in an efficient overall solution.
🌟 Today's Biggest Takeaway

Today's problem reinforced an important DSA principle:

Use one data structure to store information and another to preserve order.

In this problem:

The dictionary answers: "How many times does this character appear?"
The string answers: "Which unique character appears first?"

Learning to separate these responsibilities makes it much easier to choose the right data structures for future problems.


'''