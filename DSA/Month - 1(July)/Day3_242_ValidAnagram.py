# 242 ---> valid Anagram

#And this is how my first attemot was and guess what, it even got accepted

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)==len(t):
            letters1=list(s)
            letters2=list(t)
            letters1.sort()
            letters2.sort()
            if(letters1==letters2):
                return True
            else:
                return False
        return False
        
'''
Time Complexity
Converting strings to lists: O(n)
Sorting first list: O(n log n)
Sorting second list: O(n log n)
Comparing lists: O(n)

Overall:

Time Complexity = O(n log n)

Space Complexity

You created two additional lists:

letters1
letters2

Each stores n characters.

Space Complexity = O(n)

'''
'''
LeetCode 242 - Valid Anagram
Approach

We first check whether both strings have the same length. If their lengths are different, they cannot be anagrams, so we immediately return False.

If the lengths are equal, we convert both strings into lists of characters. We then sort both lists alphabetically. If the sorted lists are identical, it means both strings contain exactly the same characters with the same frequencies, so they are anagrams. Otherwise, they are not.

Algorithm
Check if the lengths of both strings are equal.
If the lengths are different, return False.
Convert both strings into lists of characters.
Sort both lists.
Compare the two sorted lists.
If both lists are equal, return True; otherwise, return False.

Key Learning
A string can be converted into a list of characters using list(string).
sort() modifies the original list in place and returns None.
sorted() returns a new sorted list without modifying the original.
Two lists can be compared directly using the == operator.
Before performing expensive operations like sorting, it's a good practice to handle simple edge cases (such as unequal lengths) first.
'''

# But this wasn't the optimal solution so them we come up with this one

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1={}
        dict2 = {}

        if len(s)==len(t):
            for ch in s:
                if ch in dict1:
                    dict1[ch]+=1
                else:
                    dict1[ch] = 1
        
            for ch in t:
                if ch in dict2:
                    dict2[ch]+=1
                else:
                    dict2[ch]=1
        
            return dict1==dict2
        return False

'''
LeetCode 242 - Valid Anagram (Dictionary Approach)
Approach

We first check whether both strings have the same length. If their lengths are different, they cannot be anagrams, so we immediately return False.

If the lengths are equal, we create two dictionaries to store the frequency of each character in both strings. We traverse each string and update the count of every character in its respective dictionary.

After building both dictionaries, we compare them. If both dictionaries contain the same characters with the same frequencies, the strings are anagrams and we return True; otherwise, we return False.

Algorithm
Check if the lengths of both strings are equal.
If the lengths are different, return False.
Create two empty dictionaries, dict1 and dict2.
Traverse the first string and store the frequency of each character in dict1.
Traverse the second string and store the frequency of each character in dict2.
Compare both dictionaries.
If both dictionaries are equal, return True; otherwise, return False.
Time Complexity

Let n be the length of the strings.

Checking the lengths takes O(1).
Traversing the first string takes O(n).
Traversing the second string takes O(n).
Comparing the two dictionaries takes O(n) in the worst case.

Overall Time Complexity:

O(n)

Since all operations are linear, the overall time complexity is linear.

Space Complexity

Two dictionaries are used to store the frequency of characters.

In the worst case, when every character is unique, each dictionary stores n entries.

Overall Space Complexity:

O(n)

Key Learning
Dictionaries are useful for storing the frequency of elements.
Before processing the input, always check for simple edge cases (such as unequal lengths) to avoid unnecessary computation.
Two dictionaries can be compared directly using the == operator.
For problems where the frequency of elements matters more than their order, a dictionary is often a more efficient choice than sorting.
Comparison with the Previous Approach
Approach	Time Complexity	Space Complexity
Sorting both strings	O(n log n)	O(n)
Using two frequency dictionaries	O(n)	O(n)
Improvement Achieved

✔️ Reduced the time complexity from O(n log n) to O(n) by eliminating the sorting step and using character frequency counting instead.

'''

# Further optimize the problem using this piece of code

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict={}
        

        if len(s)!=len(t):
            return False
            
        for ch in s:
            if ch in dict:
                dict[ch]+=1
            else:
                dict[ch] = 1
        
        for ch in t:
            if ch in dict:
                dict[ch]-=1
            else:
                return False
        
        for ch in dict:    
            if dict[ch]!=0:
                return False
            
        return True


'''
LeetCode 242 - Valid Anagram (One Dictionary Approach)
Approach

We first check whether both strings have the same length. If the lengths are different, the strings cannot be anagrams, so we immediately return False.

Next, we create a single dictionary to store the frequency of characters from the first string. We traverse the first string and increase the count of each character in the dictionary.

Then, we traverse the second string. For every character encountered, we decrease its corresponding count in the same dictionary. If a character from the second string does not exist in the dictionary, we immediately return False because the strings cannot be anagrams.

Finally, we traverse the dictionary and check whether every character count is zero. If any count is not zero, it means the frequencies of the characters do not match, so we return False. If all counts are zero, the strings are anagrams and we return True.

Algorithm
Check if the lengths of both strings are equal.
If the lengths are different, return False.
Create an empty dictionary to store character frequencies.
Traverse the first string and increment the count of each character in the dictionary.
Traverse the second string:
If the character exists in the dictionary, decrement its count.
If the character does not exist, return False.
Traverse all values in the dictionary.
If any value is not equal to 0, return False.
If all values are 0, return True.
Time Complexity

Let n be the length of the strings.

Length comparison takes O(1).
Traversing the first string takes O(n).
Traversing the second string takes O(n).
Traversing the dictionary to verify all counts are zero takes O(n) in the worst case.

Overall Time Complexity:

O(n)

Since each operation is linear and performed sequentially, the overall complexity remains O(n).

Space Complexity

A single dictionary is used to store the frequency of characters from the first string.

In the worst case, when every character is unique, the dictionary stores n key-value pairs.

Overall Space Complexity:

O(n)

Although only one dictionary is used instead of two, the worst-case space complexity remains O(n) because Big-O notation ignores constant factors.

Key Learning
Before processing the strings, always check simple edge cases such as unequal lengths.
A single dictionary can be used to both count and cancel out character frequencies.
Increment the frequency while traversing the first string and decrement it while traversing the second string.
If any character from the second string is missing in the dictionary, the strings cannot be anagrams.
The strings are anagrams only if every character count becomes zero after processing both strings.
Avoid returning from inside a loop unless you are certain the final answer has already been determined.
Evolution of the Solution
Approach	Time Complexity	Space Complexity
Sort both strings and compare	O(n log n)	O(n)
Two frequency dictionaries	O(n)	O(n)
One frequency dictionary	O(n)	O(n)
Improvement Achieved
✅ Eliminated the sorting step, reducing the time complexity from O(n log n) to O(n).
✅ Reduced the auxiliary memory used in practice by replacing two dictionaries with a single dictionary, while the asymptotic space complexity remains O(n).


'''
                
                
        
            
        


        

            
         

            
        