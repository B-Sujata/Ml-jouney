# First attempt

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        str1_len = len(str1)
        str2_len = len(str2)
        divisor_candidate = ""
        
        for i in range(str2_len, 0, -1):
            if str2_len%i==0:
                divisor_candidate = str2[:i]
                mul1 = str2_len//len(divisor_candidate)
                if divisor_candidate*mul1==str2:
                    divisor_candidate = divisor_candidate
                    if str1_len%i==0:
                        mul2 = str1_len//len(divisor_candidate)
                        if str1==divisor_candidate*mul2:
                            return divisor_candidate
        
        
        return ""
        

 # Final Output with generalization

 class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        str1_len = len(str1)
        str2_len = len(str2)
        divisor_candidate = ""
        if str1_len<str2_len:
            smaller = str1
            larger = str2
        else:
            smaller = str2
            larger = str1
        
        for i in range(len(smaller), 0, -1):
            if len(smaller)%i==0:
                divisor_candidate = smaller[:i]
                mul1 = len(smaller)//len(divisor_candidate)
                if divisor_candidate*mul1==smaller:
                    
                    if len(larger)%i==0:
                        mul2 = len(larger)//len(divisor_candidate)
                        if larger==divisor_candidate*mul2:
                            return divisor_candidate
        
        
        return ""
        
'''
Approach
Determine the shorter and longer string because the greatest common divisor string cannot be longer than the shorter string.
Iterate through all possible candidate lengths from the length of the shorter string down to 1 so that the first valid candidate found is the greatest divisor.
For each candidate length:
Check if it divides the length of the shorter string.
Extract the candidate substring from the beginning of the shorter string.
Repeat the candidate enough times to reconstruct the shorter string. If it cannot reconstruct the shorter string, skip it.
If the candidate successfully reconstructs the shorter string:
Check if the candidate length also divides the length of the longer string.
Repeat the candidate enough times to reconstruct the longer string.
If the candidate reconstructs both strings exactly, return it immediately since candidates are checked from largest to smallest.
If no valid candidate exists, return an empty string.
Algorithm
Find the shorter and longer strings.
Iterate i from len(shorter) down to 1.
If len(shorter) % i != 0, continue to the next iteration.

Extract the candidate substring:

candidate = shorter[:i]
Compute the number of repetitions required for the shorter string.
If repeating the candidate does not reconstruct the shorter string, continue.
If len(longer) % i != 0, continue.
Compute the number of repetitions required for the longer string.
If repeating the candidate reconstructs the longer string, return the candidate.
If the loop finishes without finding a valid candidate, return "".
Time Complexity

Let:

m = len(str1)
n = len(str2)
k = min(m, n)
Outer Loop

The loop runs at most:

k

times.

Candidate Verification

For each candidate, reconstructing the strings involves string multiplication and comparison.

Reconstructing the shorter string takes O(k).
Reconstructing the longer string takes O(max(m, n)).

Therefore, each iteration costs:

O(m + n)
Overall Time Complexity
O(k × (m + n))

where

k = min(m, n)

So the final time complexity is:

O(min(m,n)×(m+n))
	​

Space Complexity

The algorithm only uses a few variables such as:

candidate
mul1
mul2
smaller
larger

No additional data structures are used.

Ignoring the temporary strings created during slicing and string multiplication (which are language-specific implementation details), the auxiliary space complexity is:

O(1)
	​


Note: In Python, slicing (shorter[:i]) and string multiplication create temporary strings. If these temporary strings are counted, the peak extra space can be up to O(m + n) during an iteration. However, in DSA interviews and LeetCode discussions, the auxiliary space for this algorithm is typically considered O(1) because no persistent data structures proportional to the input size are maintained.

Interview Tip

If an interviewer asks, "Why do you iterate from largest to smallest?", a concise answer is:

"Since the problem asks for the greatest common divisor string, checking candidate lengths in descending order guarantees that the first valid candidate found is the largest one. This allows the algorithm to terminate early without checking smaller candidates."


'''