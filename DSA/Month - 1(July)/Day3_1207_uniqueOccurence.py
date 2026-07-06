class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}
        
        for num in arr:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1 
        
        return len(freq.values())==len(set(freq.values()))
            
            
            
        



'''
Approach

We use a dictionary to count the frequency of each element in the array.

After calculating the frequencies, we obtain all the frequency values using freq.values() and convert them into a set. Since a set stores only unique values, any duplicate frequencies will be removed.

Finally, we compare the number of frequency values in the dictionary with the number of unique frequency values in the set.

If both lengths are equal, all occurrence counts are unique, so we return True. Otherwise, at least two elements have the same frequency, so we return False.

Algorithm
Create an empty dictionary freq.
Traverse the given array.
For each number, check whether it already exists in the dictionary.
If it exists, increment its frequency by 1.
Otherwise, add it to the dictionary with an initial frequency of 1.
Obtain all frequency values using freq.values().
Convert the frequency values into a set to remove duplicate frequencies.
Compare the number of original frequency values with the number of unique frequency values.
If both lengths are equal, return True; otherwise, return False.
Time Complexity

Let n be the number of elements in the array.

Building the frequency dictionary requires traversing the entire array once, which takes O(n) time.

Creating a set from the dictionary values takes O(k) time, where k is the number of unique elements in the array. Since k ≤ n, this is at most O(n).

Therefore, the overall time complexity is:

O(n)

Space Complexity

The dictionary stores the frequency of each unique element, requiring O(k) space.

The set also stores the unique frequency values, requiring at most O(k) additional space.

Since k ≤ n, the overall auxiliary space complexity is:

O(n)

Key Learning

This problem follows a useful frequency-counting pattern:

Count frequencies → extract frequency values → remove duplicates using a set → compare sizes

The dictionary answers:

“How many times does each element occur?”

The set answers:

“Are all these occurrence counts unique?”

And this line:

return len(freq.values()) == len(set(freq.values()))

works because converting the frequencies to a set removes duplicates. If the size decreases, duplicate frequencies existed; if the size remains unchanged, all frequencies were unique.

One small precision point for your notes: your solution is O(n) time and O(n) space in the general case, and it’s a clean, optimal solution for this problem. 🔥


'''