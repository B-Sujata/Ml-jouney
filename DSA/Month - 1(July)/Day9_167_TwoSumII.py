# Earlier when I used to solve problems I used to take atleast 2 hours to solve a single problem that too with the help of AI but today I solved this problem in near about an hour that too with almost no help of AI.. And Needs to celebrate, this is a real progress

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        L = 0
        R = n-1 
        while(L<R):
            if numbers[L]+numbers[R] == target:
                return [L+1, R+1]
            elif numbers[L]+numbers[R]>target:
                R-=1
            else:
                L+=1

'''
Approach

Since the given array is sorted in non-decreasing order, we can use the Two Pointer technique.

Initialize one pointer L at the beginning of the array and another pointer R at the end.
Calculate the sum of the elements at these two pointers.
If the sum is equal to the target, we have found the required pair.
If the sum is greater than the target, move the right pointer one step to the left to decrease the sum.
If the sum is smaller than the target, move the left pointer one step to the right to increase the sum.
Continue this process until the pair is found.

This works because the array is sorted, allowing us to efficiently adjust the sum by moving only one pointer at a time.

Algorithm
Initialize two pointers:
L = 0
R = n - 1
While L < R:
Calculate numbers[L] + numbers[R].
If the sum equals the target, return the 1-based indices [L + 1, R + 1].
If the sum is greater than the target, decrement R.
Otherwise, increment L.
Since the problem guarantees exactly one solution, the correct pair will always be found.
Time Complexity

O(n)

In each iteration, either the left pointer moves one step to the right or the right pointer moves one step to the left.
Each pointer moves at most n times.
Therefore, the total number of operations is linear.
Space Complexity

O(1)

No extra data structures are used.
Only two pointer variables are maintained, so the auxiliary space remains constant.

⭐ Interview Tip: If an interviewer asks "Why does the two-pointer approach work?", mention this:

Since the array is sorted, moving the left pointer increases the sum, while moving the right pointer decreases the sum. This property allows us to eliminate impossible pairs without checking every combination, reducing the time complexity from O(n²) to O(n).


'''
                
        
            
        