class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs={
            '(':')',
            '{':'}',
            '[':']'
        }

        
        
        for i in s:
            if i in pairs:
                stack.append(i)
            else:
                if not stack :
                    return False
                if i==pairs[stack[-1]]:
                    stack.pop()
                else:
                    return False
                
        if not stack:
            return True
        
        return False

    

'''
Approach

We observe that for a valid parentheses string, the last opening bracket encountered must be the first one to be closed. This follows the Last In, First Out (LIFO) principle, making a stack the ideal data structure.

We traverse the string character by character.

If the current character is an opening bracket, we push it onto the stack.
If it is a closing bracket, we first check whether the stack is empty. If it is, there is no corresponding opening bracket, so the string is invalid.
Otherwise, we compare the current closing bracket with the expected closing bracket for the opening bracket at the top of the stack using a dictionary.
If they match, we pop the opening bracket from the stack.
If they do not match, the sequence is invalid, so we return False.
After processing all characters, if the stack is empty, every opening bracket has been matched correctly, so we return True; otherwise, we return False.
Algorithm
Create an empty stack.
Create a dictionary mapping each opening bracket to its corresponding closing bracket.
Traverse each character in the string.
If the character is an opening bracket:
Push it onto the stack.
Otherwise (it is a closing bracket):
If the stack is empty, return False.
Compare the current closing bracket with the expected closing bracket for the opening bracket at the top of the stack.
If they match, pop the top element from the stack.
Otherwise, return False.
After traversing the entire string:
If the stack is empty, return True.
Otherwise, return False.
Time Complexity

O(n)

We traverse the string only once.
Each bracket is pushed onto the stack at most once and popped at most once.
Dictionary lookup (pairs[...]) takes O(1) time.

Therefore, the total time complexity is:

O(n)

where n is the length of the input string.

Space Complexity

O(n)

In the worst case, all characters are opening brackets, for example:

((({{{[[[

All of them will be stored in the stack before any are removed.

Hence, the maximum extra space required is proportional to the number of characters.

Space Complexity = O(n)





'''