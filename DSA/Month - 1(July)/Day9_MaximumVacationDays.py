class Solution:
    def MaximumVacationDays(self, days: int, obligations:list) -> int:
        
        left = 0
        length = 0
        
        if not obligations:
            return days
        for i in range(1,days+1):
            if i not in obligations:
                diff = i - left
                if diff>length:
                    length = diff
                
            else:
                left = i+1
                

                
                
        return length
                    

'''
Pattern Recognition
Pattern:

Array Traversal / Longest Consecutive Segment

This problem does not belong to Greedy, Sliding Window, or Two Pointers.

The idea is simply to traverse all days once while keeping track of the current vacation streak and updating the maximum streak whenever a longer one is found.

How to Recognize This Pattern

Look for problems that ask you to find:

Longest consecutive sequence
Longest continuous segment
Maximum streak
Consecutive occurrences
Continuous days
Continuous subsegment (without needing to move two pointers)

Examples:

Longest streak of attendance
Maximum consecutive holidays
Longest run of 1's
Consecutive working days

Whenever you only need to scan the array once while maintaining the current streak and the maximum streak, this pattern is a good fit.

Approach

The idea is to iterate through each day from 1 to N.

If the current day is not an obligation day, it is a vacation day.
Calculate the length of the current vacation streak.
Update the maximum streak if the current streak is longer.
If the current day is an obligation day,
The current vacation streak ends.
Mark the beginning of the next possible vacation streak.

Continue this process until all days have been processed.

Algorithm
If there are no obligation days, return the total number of days.
Initialize:
left to represent the beginning of the current vacation streak.
length to store the maximum vacation streak found so far.
Traverse every day from 1 to N.
For each day:
If it is a vacation day:
Compute the current streak length.
Update the maximum streak if necessary.
Otherwise:
Reset the beginning of the next vacation streak.
Return the maximum vacation streak.
Time Complexity
O(N × M)

where

N = total number of days
M = number of obligation days

Reason:

For every day, checking

i in obligations

takes O(M) because obligations is a list.

Therefore,

N iterations × O(M)

=

O(N × M)
Can it be improved?

Yes.

If the obligations are first stored in a set, membership checking becomes O(1) on average.

Then the overall complexity becomes

O(N)

(after spending O(M) to build the set).

Space Complexity

For your current approach:

O(1)

Only a few variables (left, length, diff) are used.

If you optimize by storing obligations in a set, the space complexity becomes:

O(M)

because the set stores all obligation days.

Summary
Feature	Value
Pattern	Array Traversal / Longest Consecutive Segment
Technique	Single Pass Traversal
Time Complexity (current code)	O(N × M)
Time Complexity (using a set)	O(N)
Space Complexity (current code)	O(1)
Space Complexity (with set)	O(M)

One final note: there's a tiny off-by-one issue in your current implementation that we deliberately left for you to discover through dry-running. The pattern, approach, and complexity analysis above remain the same regardless of that small correction.

'''




