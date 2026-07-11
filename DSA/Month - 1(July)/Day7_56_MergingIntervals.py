# Honestly When I first read the problem, I though it's easy, I understood the idea and possible approach behind this, bUt I struggled a lot while implementing this one but after struggling for 2 hours striaght, I finally was able to solve this problem, Feel little good and Satisfied now, I am proud of mysef for not leaving the problem in between and sticking to it until the solution was found.
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        n = len(intervals)
        result =[intervals[0]]
        if not intervals:
            return []
        for i in range(1,n):
            if(result[-1][1]<intervals[i][0]):
                result.append(intervals[i])
            else:
                start = min(result[-1][0], intervals[i][0])
                end = max(result[-1][1], intervals[i][1])
                result[-1]=[start, end]
        return result
    
'''
Approach

The idea is to merge all overlapping intervals into a single interval.

First, sort the intervals according to their starting values. This ensures that any overlapping intervals appear next to each other.
Create a result list and add the first interval to it.
Traverse the remaining intervals one by one.
Compare the current interval with the last merged interval stored in result.
If they do not overlap, append the current interval to result.
If they do overlap, merge them by:
Taking the smaller of the two starting points.
Taking the larger of the two ending points.
Updating the last interval in result with the merged interval.
After processing all intervals, return the result list.
Algorithm
Sort the list of intervals.
Initialize a list result and insert the first interval into it.
Traverse the intervals starting from the second interval.
For each interval:
Compare the end of the last merged interval (result[-1][1]) with the start of the current interval (intervals[i][0]).
If the last merged interval ends before the current interval starts, append the current interval to result.
Otherwise:
Compute the merged interval by taking:
the minimum starting value.
the maximum ending value.
Replace the last interval in result with this merged interval.
Return result.
Time Complexity
Sorting

Sorting the intervals takes

O(nlogn)

where n is the number of intervals.

Traversing

We traverse the intervals only once.

O(n)
Total Time Complexity

The sorting step dominates the traversal.

O(nlogn)
	​

Space Complexity

We use an additional list result to store the merged intervals.

In the worst case, when no intervals overlap, all intervals are stored in result.

O(n)
	​

🌟 The Core Idea (The Invariant)

This is the one sentence that captures the entire algorithm:

At every step, result always contains the correctly merged intervals processed so far, and we only need to compare the current interval with the last merged interval (result[-1]).

This works because the intervals are sorted, so if the current interval overlaps with any previous interval, it can only overlap with the last merged interval.

'''
        
        