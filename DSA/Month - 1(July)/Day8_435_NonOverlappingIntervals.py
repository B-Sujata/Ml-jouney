# This is How my First attemp looked like

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        tracker = 0
        n = len(intervals)
        intervals.sort()
        if not intervals:
            return 0
        if n==1:
            return 0
        for i in range(n-1):
            if intervals[i][0]==intervals[i+1][0] and intervals[i][1]<=intervals[i+1][1]:
                tracker+=1
            if intervals[i][1]>(intervals[i+1][0]and intervals[i+1][1]):
                tracker+=1
            
        return tracker
    

# After Some time, finally found the right solution

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        tracker = 0
        n = len(intervals)
        intervals.sort()
        
        if not intervals:
            return 0
        if n==1:
            return 0
        prev_end = intervals[0][1]
        for i in range(n-1):
            if prev_end>intervals[i+1][0]:
                if prev_end>intervals[i+1][1]:
                    prev_end = intervals[i+1][1]
                tracker+=1
            else:
                prev_end = intervals[i+1][1]
               
            
        return tracker
        
            


'''
Approach
Sort the intervals based on their starting time.
Initialize prev_end as the end time of the first interval.
Traverse the remaining intervals one by one.
For each interval:
If it overlaps with the previously kept interval (prev_end > current_start):
One interval must be removed, so increment the removal count.
Keep the interval with the smaller end time by updating:
prev_end = min(prev_end, current_end)
Otherwise (no overlap):
Keep the current interval and update prev_end to its end time.
Return the total number of removed intervals.
Algorithm
Sort the intervals in ascending order of their start times.
If the list is empty or contains only one interval, return 0.
Set prev_end to the end time of the first interval.
Initialize tracker = 0.
Iterate through the remaining intervals:
If prev_end > current_start:
Increment tracker.
Update prev_end to the smaller of prev_end and current_end.
Else:
Update prev_end to current_end.
Return tracker.
Time Complexity
Sorting the intervals: O(n log n)
Traversing the intervals once: O(n)

Overall Time Complexity: O(n log n)

Space Complexity
No extra data structures are used apart from a few variables.

Overall Space Complexity: O(1) (excluding the space used by the sorting algorithm).



'''
            


